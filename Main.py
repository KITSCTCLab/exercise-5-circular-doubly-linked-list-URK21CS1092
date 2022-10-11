class
Node:

def __init__(self, data=None):
self.data = data
self.previous = self
self.next = self

class DoublyCircularLinkedList:
def __init__(self):
self.head = None
self.count = 0

def add_at_tail(self, data) -&gt; bool:
new_node = Node(data)
if self.count &gt; 0:
new_node.previous = self.end
self.end.next = new_node
self.head.previous = new_node
new_node.next = self.head
else:
self.head = new_node
self.end = new_node
self.count += 1
return True

def add_at_head(self, data) -&gt; bool:
new_node = Node(data)
if self.count &gt; 0:
new_node.next = self.head

new_node.previous = self.end
self.head.previous = new_node
self.end.next = new_node
else:
self.end = new_node
self.head = new_node
self.count += 1
return True

def add_at_index(self, index, data) -&gt; bool:
if index &lt; 0 or index &gt;= self.count:
return False
if index == 0:
return self.add_at_head(data)
if index == self.count:
return self.add_at_tail(data)
new_node = Node(data)
curr_node = self.head
for i in range(index):
curr_node = curr_node.next
new_node.previous = curr_node.previous
new_node.next = curr_node
curr_node.previous.next = new_node
curr_node.previous = new_node
self.count += 1
return True

def get(self, index) -&gt; int:
if index &lt; 0 or index &gt;= self.count:
return -1
curr_node = self.head

for i in range(index):
curr_node = curr_node.next
return curr_node.data

def delete_at_index(self, index) -&gt; bool:
if index &lt; 0 or index &gt;= self.count:
return False
if index == 0:
temp = self.head
temp.next.previous = self.end
self.end.next = temp.next
self.head = temp.next
self.count -= 1
return True
if index == self.count - 1:
temp = self.end
self.head.previous = temp.previous
temp.previous.next = self.head
self.end = temp.previous
self.count -= 1
return True

curr_node = self.head
for ind in range(index):
curr_node = curr_node.next
curr_node.previous.next = curr_node.next
curr_node.next.previous = curr_node.previous
self.count -= 1
return True

def get_previous_next(self, index) -&gt; list:

if index &lt; 0 or index &gt;= self.count:
return -1
curr_node = self.head
for ind in range(index):
curr_node = curr_node.next
return [curr_node.previous.data, curr_node.next.data]

# Do not change the following code
operations = []
for specific_operation in input().split(&#39;,&#39;):
operations.append(specific_operation.strip())
input_data = input()
data = []
iteration_count = 0

for item in input_data.split(&#39;, &#39;):
inner_list = []
if item.isnumeric():
data.append(int(item))
elif item.startswith(&#39;[&#39;):
item = item[1:-1]
for letter in item.split(&#39;,&#39;):
if letter.isnumeric():
inner_list.append(int(letter))
data.append(inner_list)
obj = DoublyCircularLinkedList()

result = []

for i in range(len(operations)):

if operations[i] == &quot;add_at_head&quot;:

result.append(obj.add_at_head(data[i]))

elif operations[i] == &quot;add_at_tail&quot;:

result.append(obj.add_at_tail(data[i]))

elif operations[i] == &quot;add_at_index&quot;:

result.append(obj.add_at_index(int(data[i][0]),
data[i][1]))

elif operations[i] == &quot;get&quot;:

result.append(obj.get(data[i]))

elif operations[i] == &quot;get_previous_next&quot;:

result.append(obj.get_previous_next(data[i]))

elif operations[i] == &#39;delete_at_index&#39;:

result.append(obj.delete_at_index(data[i]))

print(result)
