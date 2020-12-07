


with open('d6_input.txt', 'r') as infile:
        lines = infile.read().strip().split('\n\n') 
        count = 0

        for line in lines:
            answers = line.splitlines()
            answeredQuestions = set()
            for answer in answers:
                for question in answer:
                    answeredQuestions.add(question)

            count += len(answeredQuestions)
         
        print(count)

