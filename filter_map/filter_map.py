from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        result = []
        for item in input_array:
            boolean_value, func_result = func(item)
            if boolean_value:
                result.append(func_result)
        return result
