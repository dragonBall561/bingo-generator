def main(amount): #Since we're using this as a script that runs from another
    for i in range(0, amount):
        import random
        from random import randint

        grid = [0]*25
        for col in range(0, 5):
            nums = set()
            row = 0
            while row < 5:
                numb = random.randint(col*15 + 1, col*15 + 15)
                #Formatting...
                numb = str(numb)
                if len(numb) == 1:
                    numb = numb+" "
                #Done Formatting
                if numb in nums:
                    continue
                nums.add(numb)

                grid[row*5 + col] = numb
                row += 1

        grid[12] = 'XX'
        print("________________")
        print("|B |I |N |G |O |")
        for row in range(0, 5):
            current = grid[row*5: row*5 + 5]
            print('|' + '|'.join(current)+ '|')
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")