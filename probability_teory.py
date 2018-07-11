# Probability density function (ДФР)
import math


def uniform_pdf(x):
    return 1 if 0 <= x < 1 else 0


# Cumulative distribution function (ИФР)
def uniform_cdf(x):
    """
    Return the probability that even-distributed random value
    <= x
    """
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


# Normal distribution (ДФР норм. распр)
def normal_pdf(x, mu=0, sigma=1):
    """
                        1                 (x-U)^2
        f(x|U,S) = ————————————— * exp(- ————————— )
                   sqrt(2*pi*S)            2*S^2
    :param x: ?
    :param mu: expected value (Мат. ожидание)
    :param sigma: standard deviation
    :return: ?
    """
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (
            math.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) /
            (sqrt_two_pi * sigma)
    )


# ИФР норм. распределения
def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / (math.sqrt(2) * sigma))) / 2

# example #
# from probability_teory import normal_pdf
# from matplotlib import pyplot as plt
#
# xs = [
#     x / 10.0
#     for x in range(-50, 50)
# ]
# plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-',
#          label='мю=0, сигма=1')
# plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--',
#          label='мю=0, сигма=2')
# plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':',
#          label='мю=0, сигма=0.5')
# plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.',
#          label='мю=-1, сигма=1')
# plt.legend()
# plt.title('Несколько ДФР нормального распределения')
# plt.show()
