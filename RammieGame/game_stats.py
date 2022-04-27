class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, rammie_game):
        """Initialize statistics."""
        self.settings = rammie_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.rammie_left = self.settings.rammie_limit