from mobile_de.spiders.mobile_de_spider import MobileSpider



def main():
    # spread_mobile = SpreadMobile()
    # df_mobile = spread_mobile.df_from_worksheet(spread_mobile.connect_to_spread())
    # df_mobile.head(5)
    #
    # # get links
    # df_mobile = spread_mobile.get_links(df_mobile)
    # print(df_mobile.head(3))
    # create spider
    result_mobile = MobileSpider().parse()

    yield result_mobile


if __name__ == "__main__":
    result_mobile = main()
    print(result_mobile)





