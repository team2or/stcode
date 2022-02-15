#도서관
n,m = map(int, input().split())
books=list(map(int, input().split()))
books.sort()
left = [i for i in books if i < 0]
right= [i for i in books if i > 0]
books=[1,2,3,4,-1,-2]

left