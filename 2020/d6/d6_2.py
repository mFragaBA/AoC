


with open('d6_input.txt', 'r') as infile:
        lines = infile.read().strip().split('\n\n') 
        count = 0

        for line in lines:
            answers = line.splitlines()
            answeredByAllQuestions = set(answers[0])
            for answer in answers:
                answeredByPassanger = set()
                for question in answer:
                    answeredByPassanger.add(question)

                answeredByAllQuestions = answeredByAllQuestions.intersection(answeredByPassanger)

            count += len(answeredByAllQuestions)
         
        print(count)

