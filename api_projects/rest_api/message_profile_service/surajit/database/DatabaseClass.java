package org.surajitpatra.itm566.surajit.database;

import java.util.HashMap;
import java.util.Map;

import org.surajitpatra.itm566.surajit.model.Message;
import org.surajitpatra.itm566.surajit.model.Profile;

public class DatabaseClass {

	private static Map<Long, Message> messages = new HashMap<>();
	private static Map<String, Profile> profiles = new HashMap<>();
	
	public static Map<Long, Message> getmessages(){
		return messages;
	}
	
	public static Map<String, Profile> getprofiles(){
		return profiles;
	}
	
}
