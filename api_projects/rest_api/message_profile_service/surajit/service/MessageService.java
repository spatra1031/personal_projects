package org.surajitpatra.itm566.surajit.service;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.surajitpatra.itm566.surajit.database.DatabaseClass;
import org.surajitpatra.itm566.surajit.model.Message;

public class MessageService {
	
	
	private Map<Long, Message> messages = DatabaseClass.getmessages();
	
	
	public List<Message> getAllMessages(){
		return new ArrayList<Message>(messages.values());
	}
	
	public Message getMessage(long id) {
		return messages.get(id);
	}
	
	public Message addMessage(Message message) {
		message.setId(messages.size() + 1);
		messages.put(message.getId(), message);
		return message;
	}
	
	public Message updateMessage(Message message) {
		if (message.getId() <=0) {
			return null;
		}
		messages.put(message.getId(), message);
		return message;
	}
	
	public Message removeMessage(long id) {
		return messages.remove(id);
	}

}
