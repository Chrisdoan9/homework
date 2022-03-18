# Chris Doan homework 4.3.
expression_correlation = input("What is the value of the expression correlation (-1 to 1): ")
expression_correlation = eval(expression_correlation)
if expression_correlation > 0.9:
    shared_function = input("Is there shared function?: ")
    if shared_function == "Yes":
        print("Prediction: Interaction")
    else:
        print("Prediction: No interaction")
else:
    shared_cellular_localization = input("Is there shared cellular localization (yes/no): ")
    if shared_cellular_localization == "Yes":
        genomic_distance = input("what is the genomic distance in kb?: ")
        genomic_distance = eval(genomic_distance)
        if genomic_distance < 5:
            print("Prediction: Interaction")
        else:
            print("Prediction: No interaction")
    else:
        print("Prediction: No interaction")