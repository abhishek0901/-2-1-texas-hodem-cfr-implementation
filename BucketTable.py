import InfosetAbstraction as infoset

class BucketTable:

    def __init__(self):
        self.preflop_bucket = self.load_two_card_bucket()
        self.flop_bucket = self.load_five_card_bucket()
        return

    def load_five_card_bucket(self):
        info_set = infoset.InfosetAbstraction()
        info_set.load_model("five_card_abstraction.obj")
        return info_set

    def load_two_card_bucket(self):
        info_set = infoset.InfosetAbstraction()
        info_set.load_model("two_card_abstraction.obj")
        return info_set

    def get_bucket_id(self,card,round):
        if round == 1:  # Preflop
            bucket_id = self.corresponding_bucket(self.preflop_bucket.predict(card), round)
        else: # Flop
            bucket_id = self.corresponding_bucket(self.flop_bucket.predict(card), round)
        return bucket_id

    def corresponding_bucket(self,bucket_id,round):
        bucket_id = bucket_id[0]
        bucket_id = ('P' if round == 1 else 'F') + format(bucket_id,'03d') # Making fixed length
        return bucket_id

