import wikidata
from wikidata.client import Client

class WikiDataWrapper(wikidata.client.Client):

    # def __init__(self):
        # super(self).__init__()

    def extract_all_wikidata_parents_of_prop(self, property):
        instance_of_prop = self.get("P31") # instance of prop
        all_parents_of_relation = [c for c in relation.getlist(instance_of_prop)]

        all_parents_of_relation_marked = set([])
        while all_parents_of_relation:
            curr_prop = all_parents_of_relation.pop()
            all_parents_of_relation_marked.add(curr_prop)
            curr_prop_parents = [c for c in curr_prop.getlist(instance_of_prop)]
            all_parents_of_relation += [x for x in curr_prop_parents if x not in all_parents_of_relation_marked]

        return all_parents_of_relation_marked

if __name__ == "__main__":
    wikidata = WikiDataWrapper()
    relation = wikidata.get("P488", load=True) # chairperson property
    parents = wikidata.extract_all_wikidata_parents_of_prop(relation)
    print(parents)
