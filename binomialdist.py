# TODO: import necessary libraries
from .generaldistribution import Distribution
import math
import matplotlib.pyplot as plt


class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring

    """
    def __init__(self, mu = 0, sigma = 1, p = 0.5, n = 20):
        Distribution.__init__(self, mu, sigma)
        self.p = p
        self.n = n


    def calculate_mean(self):
        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """
        avg = 1.0 * self.p * self.n
        self.mean = avg
        return self.mean


    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        """
       self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
       return self.stdev


    def replace_stats_with_data(self):

        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """
        self.n = len(self.data)
        self.p = sum(self.data)/self.n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        return self.p, self.n


    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """
        plt.bar(self.data)
        plt.title('Bar Chart on Outcome Frequency')
        plt.xlabel('Possible Outcomes')
        plt.ylabel('Observed Frequency')


    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """
        return (math.factorial(self.n) / (math.factorial(k) * math.factorial(self.n-k)) *
                                          (self.p**k) * (1 - self.p)**(self.n - k))


    def plot_binomial_pdf(self):
        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """
        x = []
        y = []

        for k in range(0, self.n+1):
            x.append(k)
            y.append(self.pdf(k))

        plt.bar(x, y)
        plt.title('Binomial Probability Density Function')
        plt.xlabel('number of successes (k)')
        plt.ylabel('probability of k successes')

        return x, y


    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.p = (self.p + other.p)/2
        result.n = self.p + other.n
        result.mean = result.calculate_mean()
        result.stdev = result.calculate_stdev()

        return result


    def __repr__(self):
        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial object

        """
        return ("mean {}, standard deviation {}, p {}, n {}"
                .format(self.mean, self.stdev, self.p, self.n))
