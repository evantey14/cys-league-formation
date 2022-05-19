from dataclasses import dataclass
from typing import List, Set, Tuple


@dataclass(frozen=True)
class Player:
    id: int
    first_name: str
    last_name: str
    grade: int
    skill: int
    unavailable_days: List[str]
    location: Tuple[float]
    # TODO: should these fields be fixed? or extendable?

    def __repr__(self):
        return (
            f"<{self.first_name} {self.last_name} "
            f"s={self.skill} g={self.grade} {self.unavailable_days}>"
        )


class Team:
    def __init__(self, name: str, practice_day: str, location) -> None:
        self.name = name
        self.practice_day = practice_day
        self.players: Set[Player] = set()
        self.location = location
        # TODO: practice time?

    def add_player(self, player: Player) -> None:
        self.players.add(player)

    def remove_player(self, player: Player) -> None:
        self.players.remove(player)

    def get_skill(self) -> int:
        return sum([player.skill for player in self.players])

    def get_grade(self) -> float:
        return sum([player.grade for player in self.players])

    def __repr__(self):
        return (
            f"Team {self.name} {self.practice_day} ("
            f"size={len(self.players)}, "
            f"skill={self.get_skill()}, "
            f"grade={self.get_grade()/len(self.players) if len(self.players) > 0 else 0:.2f}): "
            f"{self.players}"
        )


class League:
    def __init__(self, teams: List[Team]):
        self.teams = teams

    def apply_moves(self, proposed_moves):
        for player, team_from, team_to in proposed_moves:
            if team_from is not None:
                team_from.remove_player(player)
            if team_to is not None:
                team_to.add_player(player)

    def undo_moves(self, proposed_moves):
        for player, team_from, team_to in proposed_moves:
            if team_to is not None:
                team_to.remove_player(player)
            if team_from is not None:
                team_from.add_player(player)

    def __repr__(self):
        s = f"{len(self.teams)} Teams:\n"
        for team in self.teams:
            s += f"{team}\n"
        return s
