def calculate_positive_feedback_percentage(ratings):
    if not ratings:
        return 0.0 
    
    positive_count = sum(1 for rating in ratings if rating >= 4)
    total_count = len(ratings)
    
    return (positive_count / total_count) * 100

if __name__ == "__main__":
    ratings = [5, 4, 3, 5, 2, 4, 1, 5]
    positive_feedback_percentage = calculate_positive_feedback_percentage(ratings)
    print(f"Positive Feedback: {positive_feedback_percentage:.2f}%")