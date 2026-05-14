import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import save_npz
import re
import mlflow as mf
import joblib


pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)


def load_df(path):
    dataset = os.listdir(path)[0]
    full_path = os.path.join(path, dataset)
    df = pd.read_csv(full_path)
    return df


def data_check(dataframe):
    if dataframe.isnull().sum().any():
        print("Check missings!")
    else:
        print("No missing data!")

def create_product_key(dataframe):
    dataframe["product_key"] = (
            dataframe["brand"].astype(str).str.lower().str.strip() + "_" +
            dataframe["name"].astype(str).str.lower().str.strip() + "_" +
            dataframe["category"].astype(str).str.lower().str.strip())
    return dataframe

def clean_ingredients(text):
    text = str(text).lower()
    # ci 77891 gibi yapıları ci_77891'e çevir
    text = re.sub(r"\bci\s*(\d+)\b", r"ci_\1", text)
    # Parantezleri kaldır ama içeriği koru
    text = re.sub(r"[()]", " ", text)
    # Ayraçları boşluk yap
    text = re.sub(r"[-/,.;:]", " ", text)
    # Sadece harf, sayı, underscore ve boşluk kalsın
    text = re.sub(r"[^a-z0-9_\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

class Recommender:
    def __init__(self, dataframe):
        self.df = dataframe.copy()
        self.df_rec = None
        self.tfidf = None
        self.tfidf_matrix = None
        self.cosine_similarity_matrix = None
        self.indices_map = None

    def prepare_data(self):
        self.df_rec = (
            self.df
            .drop_duplicates(subset=["product_key", "ingredients"], keep="first")
            .reset_index(drop=True)
        )

    def tfidf_vectorizer(self):
            self.tfidf = TfidfVectorizer(
                preprocessor = clean_ingredients,
                stop_words = None,
                ngram_range = (1, 2),
                min_df = 2)

            self.tfidf_matrix = self.tfidf.fit_transform(self.df_rec["ingredients"])
            return self.tfidf_matrix

    def calculate_cosine_sim(self):
        self.cosine_similarity_matrix = cosine_similarity(
            self.tfidf_matrix,
            self.tfidf_matrix
        )
        return self.cosine_similarity_matrix

    # Crates indice for each product keys in order to match each others...
    def create_indices(self):
        self.indices_map = pd.Series(self.df_rec.index, index=self.df_rec["product_key"])
        return self.indices_map

    # Controls the duplicated products... But please check the duplicateds twice and check business logis too...
    def check_duplicates(self):
        duplicated_count = self.df_rec["product_key"].duplicated().sum()

        if duplicated_count > 0:
            print("More item exist! investigate if it is normal or not...")
        else:
            print("Not more than one!")

    def process_duplicates(self):
        duplicates = self.df_rec[self.df_rec["product_key"].duplicated(keep=False)][
            ["brand", "name", "category", "size", "product_key"]
            ].sort_values("product_key")
        self.check_duplicates()
        return duplicates

    def fit(self):
        self.prepare_data()
        self.tfidf_vectorizer()
        self.calculate_cosine_sim()
        self.create_indices()


    def recommend(self, product_name, top_n=5):
        product_name = product_name.lower().strip()

        matches = self.df_rec[
            self.df_rec["name"]
            .str.lower()
            .str.strip()
            .str.contains(product_name, na=False)
        ]

        if matches.empty:
            return "Product not found."

        product_index = matches.index[0]

        similarity_scores = pd.DataFrame(self.cosine_similarity_matrix[product_index],columns=["score"])

        product_indices = (similarity_scores.sort_values("score", ascending=False).iloc[1:top_n + 1].index)

        return self.df_rec.loc[product_indices,["brand", "name", "category", "price", "size"]]

    def save_artifacts(self, artifacts_path="../artifacts/recommender"):
        os.makedirs(artifacts_path, exist_ok=True)
        joblib.dump(
            self.tfidf,
            f"{artifacts_path}/tfidf_vectorizer.pkl"
        )
        save_npz(
            f"{artifacts_path}/tfidf_matrix.npz",
            self.tfidf_matrix
        )
        joblib.dump(
            self.indices_map,
            f"{artifacts_path}/indices.pkl"
        )
        self.df_rec.to_csv(
            f"{artifacts_path}/df_rec.csv",
            index=False
        )


if __name__ == "__main__":
    mf.set_tracking_uri("sqlite:///mlflow.db")
    mf.set_experiment("recommender_v00")

    with mf.start_run(run_name="recommender_v00"):
        path = "data/raw"

        df = load_df(path)
        df = create_product_key(df)
        data_check(df)

        rec = Recommender(df)
        rec.fit()
        rec.save_artifacts("artifacts/recommender")

        mf.log_param("vectorizer", "TfidfVectorizer")
        mf.log_param("ngram_range", "(1, 2)")
        mf.log_param("min_df", 2)
        mf.log_param("similarity_metric", "cosine_similarity")

        mf.log_artifacts("artifacts/recommender")








