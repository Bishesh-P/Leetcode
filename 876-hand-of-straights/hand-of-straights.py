class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        # HashMap: count frequency
        count = {}

        for card in hand:
            count[card] = count.get(card, 0) + 1

        # Process cards from smallest to largest
        for card in sorted(count):

            if count[card] > 0:
                start_count = count[card]

                for x in range(card, card + groupSize):

                    if x not in count or count[x] < start_count:
                        return False

                    count[x] -= start_count

        return True