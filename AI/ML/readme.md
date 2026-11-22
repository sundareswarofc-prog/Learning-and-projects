                                     Lesson-1


* What is Artificial Intelligence?
     Artificial Intelligence (AI) is a technology that allows computers to perform tasks that normally require human intelligence.

       For example:
         - Understanding human language.
         - Recognizing images.
         - Answering questions.
         - Predicting future outcomes.
         - Making decisions.
         - Generating computer code.

* Concept	                Meaning
   AI	                  Making computers perform intelligent tasks
   ML	                  Teaching computers to learn patterns from data
   Deep Learning	      Using multi-layer neural networks to learn complex patterns

* Important Machine Learning types
    There are three major types of Machine Learning.

      1. Supervised Learning
      
          The model learns from data that already has correct answers (labels).
          
          Example: Predicting house prices or identifying spam emails.
      
      2. Unsupervised Learning
      
           The model finds patterns in data without predefined answers.
           
           Example: Grouping customers based on purchasing behavior.
      
      3. Reinforcement Learning
      
            The model learns through actions, rewards and penalties.
            
            Example: Training an AI to play chess.

* How Machine Learning actually works

   1. What is a Dataset?
        A dataset is a collection of information used to train a Machine Learning model.

   2. What are Features and Labels?
        This is a very important Machine Learning concept.

          Features (Input data)

            These are the values we give to the model.
              - Study hours
              - Attendance
            
          Label (Expected output)
            
            This is the value we want the model to predict.
              - Marks

          example:
                    X = [ 
                [2, 70],    
                [4, 80],
                [5, 90],
                [6, 95],
                [3, 75] 
            ]  -> (INPUT)

            y = [35, 55, 70, 85, 45] -> (OUTPUT)

    3. What is Training?
         Training means teaching a Machine Learning model using existing data.

         The model analyzes these examples and learns patterns.

         It tries to understand how input values relate to output values.
    
    4. What is Testing?
         After training, we need to check whether the model can predict results for data it has never seen before.
         This is called testing.

         for  example :
            study_hours = [2, 4, 5, 6, 3]
            marks = [35, 55, 70, 85, 45]

            New data: study hours = 7

            Now the model can predict the output

* What is a Machine Learning algorithm?
    An algorithm is a method that a computer uses to learn patterns from data.

    For example, imagine you want to build an application that predicts house prices.

* Two important ML problem types

  1. Regression

   Predicts a numerical value.

    Examples:
        - House price prediction.
        - Student marks prediction.
        - Monthly sales prediction.
 
  2. Classification

    Predicts a category or class.

        Examples:
        - Spam or Not Spam.
        - Pass or Fail.
        - Fraud or Not Fraud.

                         
                                 Lesson -3

 * Types of Machine Learning Algorithm

  1. What is a Machine Learning algorithm?
        An algorithm is a method that a computer uses to learn patterns from data.

  2. Two important ML problem types
        Before learning algorithms, understand these two categories.

        * Regression

          Predicts a numerical value.

          Examples:
          - House price prediction.
          - Student marks prediction.
          - Monthly sales prediction.

        * Classification

            Predicts a category or class.

            Examples:
            - Spam or Not Spam.
            - Pass or Fail.
            - Fraud or Not Fraud.

  3. Important Machine Learning algorithms

        Let's understand five commonly used algorithms.
           Algorithm 1: Linear Regression
           Algorithm 1: Logistic Regression
           Algorithm 1: Decision Tree 
           Algorithm 1: Random Forest
           Algorithm 1: K-means clustering

      * Linear Regression
            Used to predict numerical values.
             Example: Predict student marks based on study hours.

          How does it work?
             It learns a mathematical relationship between input and output.

      * Logistic Regression
           Despite having "Regression" in its name, Logistic Regression is commonly used for classification.
             Example: Predict whether a student passes or fails.
          
      * Decision Tree
           * A Decision Tree makes predictions using a sequence of questions and decisions.
           * Decision Trees can be used for both classification and regression.

      * Random Forest
           * Random Forest is a collection of multiple Decision Trees.
           * Instead of depending on one tree, it uses multiple trees and combines their predictions.
      
      * K-Means Clustering
           * K-Means groups similar data points together.
           * Unlike the previous examples, it does not require labels.
              Example: Grouping customers based on their spending habits.