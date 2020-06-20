import math
import matplotlib.pyplot as plt

class Gaussian():
    """ Gaussian distribution class for calculating and
    visualizing a Gaussian distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file

    """
    def __init__(self, mu = 0, sigma = 1):

        self.mean = mu
        self.stdev = sigma
        self.data = []
        #data_len = len(self.data)


    def calculate_mean(self):

        """Method to calculate the mean of the data set.

        Args:
            None

        Returns:
            float: mean of the data set

        """

        sums = 0
        mu = self.mean
        data_list = self.data

        for nums in data_list:
            sums += nums

        mu = sums/len(data_list)

        return mu


    def calculate_stdev(self, sample=True):

        """Method to calculate the standard deviation of the data set.

        Args:
            sample (bool): whether the data represents a sample or population

        Returns:
            float: standard deviation of the data set

        """

        sqrt = math.sqrt
        total = 0

        for x in self.data:
            total += pow((x - self.calculate_mean()), 2)

        if sample == True:
            self.stdev = sqrt(total/(len(self.data) - 1))

        else:
            self.stdev = sqrt(total/(len(self.data)))

        return self.stdev


    def read_data_file(self, file_name, sample=True):

        """Method to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.
        After reading in the file, the mean and standard deviation are calculated

        Args:
            file_name (string): name of a file to read from

        Returns:
            None

        """

        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()


    def plot_histogram(self, file_name="Data List"):
        """Method to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        file_name = file_name
        data_list = self.data
        n_bins = len(data_list)
        plt.hist(x=data_list, bins=n_bins, facecolor='blue')

        #plt.legend(prop ={'size': 10})
        plt.xlabel("Number Entries")
        plt.ylabel("Frequency of Number Entries")
        plt.title("Histogram Plot of {}"
                  .format(file_name),
                  fontweight ="bold")

        plt.show()


    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.

        Args:
            x (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """

        _sqrt = math.sqrt
        _pi = math.pi
        _e = math.e
        mu = self.mean
        sigma = self.mean

        return (1/(sigma*_sqrt(2*_pi))) * (pow(_e, ((-1/2)*((x - mu)/sigma)**2)))


    def plot_histogram_pdf(self, n_spaces = 50):

        """Method to plot the normalized histogram of the data and a plot of the
        probability density function along the same range

        Args:
            n_spaces (int): number of data points

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)

        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data, µ = {} σ = {}'
                          .format(mu, sigma))
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y
