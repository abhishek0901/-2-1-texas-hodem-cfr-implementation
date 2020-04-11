import BucketTable as bt

bt = bt.BucketTable()
print(bt.get_bucket_id([[3,3,3,10,2,4,2,11,2,13]],2) == 'F544')