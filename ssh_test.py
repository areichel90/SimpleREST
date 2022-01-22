import pandas as pd

if __name__ == "__main__":
    print("Nice.")

    dict = {1: "a", 2: "b"}
    df_test = pd.DataFrame.from_dict(dict, orient="index")
    print(df_test)
