from matplotlib import pyplot as plt

###########
# Justin Bloss
# CIS 312
###########
# Scatterplot program
# The scatterplot program will replicate a scatterplot that takes into account
# amount of time studied v average score and plot them within the graph. The
# purpose of the program is to learn how to create and modify graphs within
# python.
def main():
    # array for time studied by students
    time_studied = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    # array for average scores per student
    average_scores = [17.1, 6.4, 9.2, 15.1, 14.2, 18.2, 20.3, 16.6, 15.9, 21.3]
    
    # create a scatterplot with x axis for time studied and y axis for average
    # score
    plt.scatter(time_studied, average_scores)
    
    # setting scatterplot title
    plt.title("Time Studying vs. Quiz Scores")
    
    # x and y axis labels to keep consistent with assigned variables
    plt.xlabel("time studied")
    plt.ylabel("quiz scores")
    
    # draw the plot
    plt.draw()
    # show the plot
    plt.show()
    
main()
    