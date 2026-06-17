from collections import defaultdict


def find_itinerary(tickets):
    if not tickets:
        return []

    def generate_itinerary(orign):
        destination_list = routes[orign]
        while destination_list:
            nxt = destination_list.pop()
            generate_itinerary(nxt)
        itinerary.append(orign)

    itinerary = []
    routes = defaultdict(list)
    for origin, destination in tickets:
        routes[origin].append(destination)

    for origin, destinations in routes.items():
        destinations.sort(reverse=True)

    generate_itinerary("JFK")
    return itinerary[::-1]


if __name__ == '__main__':
    tkts = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    tkts1 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    tkts2 = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]

    print(find_itinerary(tkts2))
