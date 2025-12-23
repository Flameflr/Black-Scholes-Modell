import math
from scipy.stats import norm


def blackscholesmodell (A, K, r, vol, t, option): # A = underlying price (Aktienkurs); K = strike Value; r = riskfree Rate; t = Time (in years)
    
    # Second Part:
    
    # 2.1: discounted strike price
    discount = K * math.exp(-r * t)

    # 2.2: probability that strike price will be reached

    # 2.2.1: required return (German: benötigte Rendite)
    rd = math.log(A/K)

    # 2.2.2: expected return (German: Erwartbare Rendite)
    expRet = (r - vol ** 2 / 2) * t

    probStrikepriceReached = (rd + expRet) / (vol * math.sqrt(t))

    # First part:
    
    # 1.1: if the strike price got reached, how far is the underlying price t1 above the strike price (Wie weit ist die Option im Geld, falls der Strike Price erreicht wurde)
    HowFarInProfit = (rd + (r + vol ** 2 / 2) * t) / (vol * math.sqrt(t))

    if option == "call":
        return A * norm.cdf(HowFarInProfit) - discount * norm.cdf(probStrikepriceReached)

    elif option == "put":
        return discount * norm.cdf(-probStrikepriceReached) - A * norm.cdf(-HowFarInProfit)

print(blackscholesmodell(45, 50, 0.018, 0.3, 0.5, "call"))
print(blackscholesmodell(45, 50, 0.018, 0.3, 0.5, "put"))
