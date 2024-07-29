from typing import (
    Dict,
    List,
    Optional,
    Tuple,
)

import poetry_version

__version__ = poetry_version.extract(source_file=__file__)


def run_turing_machine(
    machine: Dict,
    input_: str,
    steps: Optional[int] = None,
) -> Tuple[str, List, bool]:
    final_state = machine['final states']
    actual_state = machine['start state']
    transition_table = machine['table']

    line=input_
    i = 0
    history = []
    step = 0
    while steps is None or step < steps:
        if i >= len(line):
            line= line+machine['blank']
        if i < 0:
            line=machine['blank'] + line
            i = 0
        actual_symbol = line[i]
        if actual_state in transition_table and actual_symbol in transition_table[actual_state]:
            transition = transition_table[actual_state][actual_symbol]
            history.append({
                "state": actual_state,
                "reading": actual_symbol,
                "position": i,
                "memory": line,
                "transition": transition
            })
            if isinstance(transition, dict):
                if 'write' in transition:
                    line = line[:i] + transition['write'] + line[i+1:]
                if 'R' in transition:
                    actual_state = transition['R']
                    i += 1
                if 'L' in transition:
                    actual_state = transition['L']
                    i -= 1
            else:
                if transition == "R":
                    i += 1
                if transition == "L":
                    i -= 1
            step += 1
            if actual_state in final_state:
                break
        else:
            history.append({
                "state": actual_state,
                "reading": actual_symbol,
                "position": i,
                "memory": line,
                "transition": transition
            })
            break
    return (line.strip(machine['blank']), history, actual_state in final_state)
