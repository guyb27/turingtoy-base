import json
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
    #pass  # Implement the function

    i = 100;
    i_min = 100;
    i_real = 100
    history=[]
    next_state = machine["start state"]
    actual_state = next_state
    my_input = machine["blank"] * 100 + input_
    while next_state not in machine["final states"]:
        if i > len(my_input)-1:
            my_input = my_input + str(machine["blank"])
        actual_state = machine["table"][next_state][my_input[i]]


        curr = {
            "state": next_state,
            "reading": my_input[i],
            #"position": i-1000 if i-1000 >= 0 else 0,
            "position": i_real,
            "memory": my_input[i_min:].strip(),
            "transition": {
            }
        }
        if "write" in actual_state:
            my_input = my_input[0:i] + actual_state["write"] + my_input[i+1:]
            curr["transition"]["write"]=actual_state["write"]
        side = ""
        if "R" in actual_state:
            i+=1
            if i_real <= len(input_)-1:
                i_real+=1
            side = "R"

        elif "L" in actual_state:
            if i_real > 0:
                i_real -=1
            i-=1
            side = "L"
        if isinstance(actual_state, dict):
            curr["transition"][side]=actual_state[side]
            next_state=actual_state[side]
        else:
            curr["transition"]=actual_state
        history.append(curr)
        #print (curr)
        if i < i_min:
            i_min=i

    #print(next_state)
    #print("OUTPUT:")
    #print("["+my_input+"]")
    return (my_input[i_min:].strip(), history, True,)
