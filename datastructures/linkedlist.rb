class Node
    attr_accessor :next_node
    attr_reader :value

    def initialize(value)
        @value = value
        @next_node = nil
    end

end

class LinkedList

    def initialize(value)
        @head = nil
    end

    def append(value)
        if @head
            find_tail.next_node = Node.new(value)
        else
            @head = Node.new(value)
        end
    end

    def find_tail
        node = @head

        return node if !node.next_node
        return node if !node.next_node while (node = node.next_node)
    end

    def append_after(target, value)
        node = find(target)
        return unless node

        old_next = node.next_node
        node.next_node = Node.new(value)
        node.next_node.next_node = old_next
    end

    def find(value)
        node = @head

        return false if !node.next_node
        return node if node.value == value
        while (node = node.next_node)
            return node if node.value == value
        end
    end

    def delee(value)
        if @head.value = value
            @head = @head.next_node
            return
        end

        node = find_before(value)
        node.next_node = node.next_node.next_node
    end

    def find_before(value)
        node = @head
        return false if !node.next_node
        return node if node.next_node.value == value

        while (node = node.next_node)
            return node if node.next_node && node.next_node.value == value
        end
    end

    def print
        node = @head
        puts node
        while (node = node.next_node)
            puts node
        end
    end
    
end