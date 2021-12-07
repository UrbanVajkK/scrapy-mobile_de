from spread_mobile import SpreadMobile
from mobile_de_spider import Mobile_deSpider
import pickle


def main():
    spread_mobile = SpreadMobile()
    df_mobile = spread_mobile.df_from_worksheet(spread_mobile.connect_to_spread())
    df_mobile.head(5)

    # get links
    df_mobile = spread_mobile.get_links(df_mobile)
    print(df_mobile.head(3))
    # create spider
    pickle_mobile = Mobile_deSpider(start_urls=df_mobile).parse(df_mobile)

    return pickle_mobile, df_mobile


if __name__ == "__main__":
    pickle_mobile, df_mobile = main()


pickle.dump(pickle_mobile, open("mobile_de.idx", "wb"))


