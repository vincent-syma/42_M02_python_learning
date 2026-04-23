from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Tournament platform management system"""

    def __init__(self) -> None:
        self.cards = {}
        self.counters = {}
        self.matches = 0

    def register_card(self, card: TournamentCard) -> str:
        """Adds TournamentCard to the tournament and assigns ID to it"""

        key = card.name.split()[-1].lower()

        if key not in self.counters:
            self.counters[key] = 0

        self.counters[key] += 1

        card_id = f"{key}_{self.counters[key]:03}"

        self.cards.update({card_id: card})
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Compares rating of card1 and card2.
        Wins the one with higher rating."""

        self.matches += 1

        card1_rating = self.cards[card1_id].calculate_rating()
        card2_rating = self.cards[card2_id].calculate_rating()

        if card1_rating > card2_rating:
            winner_id, loser_id = card1_id, card2_id

        elif card1_rating < card2_rating:
            winner_id, loser_id = card2_id, card1_id

        else:
            winner_id, loser_id, winner_rating, loser_rating = None

        if winner_id and loser_id:
            self.cards[winner_id].update_wins(1)
            self.cards[loser_id].update_losses(1)
            winner_rating = self.cards[winner_id].calculate_rating()
            loser_rating = self.cards[loser_id].calculate_rating()

        return {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner_rating,
            'loser_rating': loser_rating
        }

    def get_leaderboard(self) -> list:
        """Sorts all participants from the highest rating in one list."""

        leaderboard = sorted(self.cards.values(),
                             key=lambda card: card.calculate_rating(),
                             reverse=True)
        return leaderboard

    def generate_tournament_report(self) -> dict:
        """Generates tournament statistics."""

        total_cards = len(self.cards.values())
        avg_rating = round(sum(card.calculate_rating()
                               for card in self.cards.values())
                           / total_cards)

        return {
            'total_cards': total_cards,
            'matches_played': self.matches,
            'avg_rating': avg_rating,
            'platform_status': 'active'
        }
