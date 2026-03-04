questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 1],
    ["What is the capital of France?", "Rome", "Paris", "London", "Berlin", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2],
    ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Shark", 2],
    ["Who wrote 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Homer", 1],
    ["What is the square root of 64?", "6", "8", "10", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "China", "Japan", "South Korea", "India", 1],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 2],
    ["What is the fastest land animal?", "Cheetah", "Lion", "Elephant", "Horse", 0],
    ["Which ocean is the largest?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 3],
    ["What is the smallest country in the world?", "Vatican City", "Monaco", "San Marino", "Liechtenstein", 0],
]
prizes = [10000, 32000, 400000, 450000, 500000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000]
i = 0
for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d\n"))

    if question[5] == a-1:
        print("Correct Answer")
    else:
        print(f"Incorrect, the correct answer was {question[5]}")
        print("Better luck next time")
        break

    print(f"You won {prizes[i]}")
    i += 1
