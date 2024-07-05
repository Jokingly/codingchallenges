"""
Description:

For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.

The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant.

The following are some examples of how this class is used:

var helper = new PaginationHelper(['a','b','c','d','e','f'], 4);
helper.pageCount(); // should == 2
helper.itemCount(); // should == 6
helper.pageItemCount(0); // should == 4
helper.pageItemCount(1); // last page - should == 2
helper.pageItemCount(2); // should == -1 since the page is invalid

// pageIndex takes an item index and returns the page that it belongs on
helper.pageIndex(5); // should == 1 (zero based index)
helper.pageIndex(2); // should == 0
helper.pageIndex(20); // should == -1
helper.pageIndex(-10); // should == -1

"""

# Revised Solution
# TODO: complete this class

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        if self.item_count() % self.items_per_page == 0:
            return self.item_count() / self.items_per_page
        else:
            return self.item_count() // self.items_per_page + 1
        
    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):            
        if page_index >= self.page_count() or page_index < 0:
            return -1
        
        elif page_index < (self.page_count() - 1):
            return self.items_per_page
        
        elif page_index == (self.page_count() - 1):
            return self.item_count() % self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index >= self.item_count() or item_index < 0:
            return -1 
        else:
            return item_index // self.items_per_page


# First Solution
# TODO: complete this class
import math

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.temp_list = []
        self.shallow_copy = list(collection).copy()
    
        while len(self.shallow_copy) > 0:
            i = 0
            l = []
            while i < items_per_page and len(self.shallow_copy) != 0:

                l.append(self.shallow_copy.pop(0)) # throws error, once list is empty
                i += 1

            self.temp_list.append(l)

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return math.ceil(len(self.temp_list))

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
                 
        try: 
            return len(self.temp_list[page_index])
                
        except:
            return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        print(item_index)
        if item_index < 0:
            return -1 
        
        count = len(self.temp_list)
        
        for i in range(len(self.temp_list)):
            try: 
                if self.collection[item_index] in self.temp_list[i]:
                    '''print('collection input:', self.collection, ', items per page:', self.items_per_page)
                    print('page_index input:', item_index, ', number at index:', self.collection[item_index])
                    print('processed collection:', self.temp_list)
                    print('returned value:', i)'''
                    return i
                  
            except:
                count -= 1

        if count == 0:
            return -1


