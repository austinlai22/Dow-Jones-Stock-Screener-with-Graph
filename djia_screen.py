#code


stock_list=[("AAPL", 37.72, 28.46, 2.98, 7.68, 32.18, 35.54, 1.73, 17.6, 75.2, 31.7, 0.67, 67.87),
           ("CRM", 133.89, 63.62, 9.26, 9.84, 5.04, 56.05, 0, 6.3, 9.7, -0.7, 0, 37.06),
           ("MSFT", 33.97, 28.18, 2.34, 10.81, 12.91, 47.14, 0.6, 16.2, 40.7, 23.1, 1.06, 33.49),
           ("MCD", 31.75, 24.97, 5.74, 8.08, -10000, 296, -10000, 9.9, -55.6, 27.4, 2.48, 5.28),
           ("INTC", 9.85, 11.03, 1.24, 2.59, 2.82, 13.7, 0.49, 15.1, 28.3, 17.8, 2.63, -16.02),
           ("WMT", 21.23, 25.55, 3.12, 0.76, 5.12, 23, 0.62, 8.2, 26.4, 12.1, 1.47, 23.73),
           ("CSCO", 17.99, 13.16, 2.93, 3.87, 4.91, 20.35, 0.38, 11.3, 28.4, 20.7, 3.25, -7.59),
           ("PG", 25.91, 22.92, 3.06, 4.61, 7.12, 46.58, 0.67, 11.5, 29.7, 16.1, 2.33, 8.49),
           ("HD", 22.89, 21.39, 3.01, 2.3, 185.18, 24.4, 23.01, 20.8, -910.8, 43.6, 2.27, 21.26),
           ("GS", 14.1, 10.13, 1.35, 1.52, 1.07, 6.43, 8.19, 0.6, 7.8, 1.3, 2.05, 6.29),
           ("MMM", 20.33, 18.37, 5.09, 3.14, 8.44, 33.79, 1.65, 10.9, 46.2, 16.4, 3.39, -1.66),
           ("NKE", 82.09, 37.28, 3.27, 5.77, 23.28, 427.81, 1.03, 9.2, 30.2, 13.3, 0.8, 35.8),
           ("MRK", 18.25, 13.04, 2.72, 4.41, 7.19, 318.16, 0.98, 13.2, 42.3, 19.2, 3.13, -8.75),
           ("DOW", -10000, 20.04, -10000, 1.03, 3.26, 6.01, 1.41, -3.9, -18.2, -4.4, 5.14, -0.55),
           ("VZ", 13.68, 12.09, 6.03, 1.96, 3.85, 21.81, 1.78, 6.2, 29.4, 13.7, 4.15, -1.45),
           ("V", 45.62, 30.53, 3.79, 19.83, 13.15, 61.55, 0.77, 13.7, 34.8, 20.2, 0.62, 10.49),
           ("JNJ", 24.36, 16.92, 5.56, 4.92, 6.22, 49.78, 0.59, 10.6, 27.4, 17.3, 2.65, 4.37),
           ("AMGN", 18.4, 13.42, 2.77, 5.26, 12.18, 20.07, 3.13, 11.7, 72.1, 21.2, 2.81, -5.36),
           ("UNH", 19.52, 18.69, 1.56, 1.27, 4.95, 20.42, 0.67, 9, 27.5, 16.2, 1.47, 15.54),
           ("IBM", 13.94, 10.72, -10000, 1.44, 5.25, 14.44, 3.08, 5.1, 38.3, 11.4, 5.22, -6.77),
           ("CVX", -10000, 35.05, -10000, 1.66, 1.31, -10000, 0.26, -5, -8.3, 0.2, 5.53, -22.54),
           ("KO", 27.52, 25.14, 9.63, 6.68, 12.25, 105.1, 2.84, 9, 45.5, 12, 3.09, -4.16),
           ("TRV", 15.65, 13.09, 3.5, 1.08, 1.24, 6.64, 0.25, 2, 8.5, 9.1, 2.49, -0.18),
           ("HON", 31.5, 26.84, 14.83, 4.38, 8.24, 57.67, 1.23, 8.2, 27.5, 17.2, 1.75, 19.76),
           ("JPM", 15.69, 13.22, -10000, 5.2, 1.54, -10000, 1.16, 0.8, 10.1, 8.3, 2.99, -13.72),
           ("CAT", 29.74, 24.24, -10000, 2.13, 6.49, 27.24, 2.55, 4.3, 23.1, 12.2, 2.3, 21.11),
           ("WBA", 84.31, 8.04, 12.06, 0.25, 1.75, 15.05, 0.81, 0.5, 2.1, 2.4, 4.49, -29.36),
           ("DIS", -10000, 32.27, -10000, 4.26, 3.35, 138.59, 0.71, -1.4, -3.3, -1.9, 0, 6.96),
           ("BA", -10000, 161.79, -10000, 2.13, -10000, -10000, -10000, -3, 42.7, -1.9, 0, -28.04),
           ("AXP", 30.08, 18.02, 3.25, 2.46, 4.48, 40.03, 6.03, 1.7, 15.1, 4.2, 1.41, -2.13)]
           
def sort():
    for metric in stock_list:
        l.append((metric[sorter],metric[0]))
        m.append((metric[sorter],metric[0]))
        if sorter == 8 or sorter == 9 or sorter == 10 or sorter ==  11 or sorter ==  12:
            l.sort(reverse = True)
        else:
            l.sort()
    for (x, stock) in l:
        stocksvalue.append(x)
        stocksname.append(stock)
    for (x, stock) in m:
        graphlist.append(x)
        graphnames.append(stock)  
    if sorter == 1 or sorter == 2 or sorter == 3 or sorter == 4 or sorter == 5 or sorter == 6 or sorter == 7:
        while (-10000 in stocksvalue) == True:
            for i in stocksvalue:
                if i == -10000:
                    k = stocksvalue.index(-10000)
                    int(k)
                    stocksvalue.pop(k)
                    stocksname.pop(k)
        while (-10000 in graphlist) == True:
            for i in graphlist:
                if i == -10000:
                    k = graphlist.index(-10000)
                    int(k)
                    graphlist.pop(k)
                    graphnames.pop(k)
    for i in range(0,len(stocksname)):
        print(1+i,":",stocksname[i])
    import matplotlib.pyplot as plt
    fig = plt.figure()
    graph = fig.add_axes([0,0,2,2])
    graph.scatter(graphnames, graphlist, color="r")
    graph.set_xlabel("Stocks")
    graph.set_title("Scatter Plot of DJIA Stocks by a Certain Metric")
    if sorter == 1:
        graph.set_ylabel("P/E Ratio")
    if sorter == 2:
        graph.set_ylabel("Forward P/E Ratio")
    if sorter == 3:
        graph.set_ylabel("PEG Ratio")
    if sorter == 4:
        graph.set_ylabel("P/S Ratio")
    if sorter == 5:
        graph.set_ylabel("P/S Ratio")
    if sorter == 6:
        graph.set_ylabel("P/FCF Ratio")
    if sorter == 7:
        graph.set_ylabel("D/E Ratio")
    if sorter == 8:
        graph.set_ylabel("ROA (%)")
    if sorter == 9:
        graph.set_ylabel("ROE (%)")
    if sorter == 10:
        graph.set_ylabel("ROI (%)")
    if sorter == 11:
        graph.set_ylabel("Dividend yield (%)")
    if sorter == 12:
        graph.set_ylabel("Performance YTD (%)")

l = []
m = []
stocksname = []
stocksvalue = []
graphlist = []
graphnames = []
sorter = int(input("Sort stocks by: ('1' for P/E, '2' for Forward P/E, '3' for PEG, '4' for P/S, '5' for P/B, '6' for P/FCF, '7' for Debt-to-Equity, '8' for Return on Assets, '9' for Return on Equity, '10' for Return on Investment, '11' for Dividend Yield %, '12' for Performance YTD %)\t"))
sort()
