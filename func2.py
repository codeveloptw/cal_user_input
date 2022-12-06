# 寫一個function來算出清單中數字的總數
# function應該要有一個參數讓使用者投入（傳遞進去）一個清單，
# function應該回傳(return)清單中數字的總數。
# 請把function命名為sum_of_list  ，這樣才可以執行測試。（P.S.  sum 就是"總數"的意思）

def sum_of_list(numbers):
	return sum(numbers)
	
user_input = input('輸入數字串計算總數: ')
numbers = list(map(int,user_input.split()))
print(numbers)
print(f'sum = {sum_of_list(numbers)}')
