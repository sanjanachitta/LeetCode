class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        dict1 = {}

        # Build frequency dictionary for license plate
        for i in licensePlate:
            if i.isalpha():
                i = i.lower()

                if i in dict1:
                    dict1[i] += 1
                else:
                    dict1[i] = 1

        answer = ""

        # Check every word
        for word in words:
            dict2 = {}

            for k in word.lower():
                if k in dict2:
                    dict2[k] += 1
                else:
                    dict2[k] = 1

            # Check whether word contains all required letters
            complete = True

            for key, value in dict1.items():
                if key not in dict2 or dict2[key] < value:
                    complete = False
                    break

            # If completing, check whether it is shorter
            if complete:
                if answer == "" or len(word) < len(answer):
                    answer = word

        return answer