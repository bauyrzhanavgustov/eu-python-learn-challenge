class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        if not input_list:
            return input_list

        max_value = max(input_list)

        replaced_list = list(map(lambda x: max_value if x > 0 else x, input_list))

        return replaced_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        low = 0
        high = len(input_list) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_value = input_list[mid]

            if mid_value == query:
                return mid
            elif mid_value < query:
                low = mid + 1
            else:
                high = mid - 1

        return -1
