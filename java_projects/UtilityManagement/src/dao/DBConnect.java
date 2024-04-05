package dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import models.ManageUtilityIncident;

public class DBConnect {
    protected Connection connection;

    public Connection getConnection() {
        return connection;
    }

    private static final String URL = "jdbc:mysql://www.papademas.net:3307/510fp";
    private static final String USERNAME = "fp510";
    private static final String PASSWORD = "510";

    public DBConnect() {
        try {
            connection = DriverManager.getConnection(URL, USERNAME, PASSWORD);
        } catch (SQLException e) {
            System.out.println("Error creating a connection to the database: " + e);
            System.exit(-1);
        }
    }

    public void closeConnection() {
        try {
            if (connection != null && !connection.isClosed()) {
                connection.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public boolean authenticateAdmin(String username, String password) {
    	//DBConnect dbConnect = new DBConnect(); 
    	
        // Query the database to check if the entered credentials are valid
        String query = "SELECT * FROM ums_admin_login WHERE username = ? AND password = ?";
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setString(1, username);
            statement.setString(2, password);
            ResultSet resultSet = statement.executeQuery();
            return resultSet.next(); // Returns true if there is a matching record
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }
    
    public boolean authenticateUser(String username, String password) {
    	//DBConnect dbConnect = new DBConnect(); 
    	
        // Query the database to check if the entered credentials are valid
        String query = "SELECT * FROM ums_user_login WHERE username = ? AND password = ?";
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setString(1, username);
            statement.setString(2, password);
            ResultSet resultSet = statement.executeQuery();
            return resultSet.next(); // Returns true if there is a matching record
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }
    
    public void adminSignUp(String username, String password, String name, String email, int age, String city, String state, int zipcode) throws SQLException {
        String sql = "INSERT INTO ums_admin_login (username,password,name, email, age, city, state, zipcode) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";

        try (PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setString(1, username);
            statement.setString(2, password);
            statement.setString(3, name);
            statement.setString(4, email);
            statement.setInt(5, age);
            statement.setString(6, city);
            statement.setString(7, state);
            statement.setInt(8, zipcode);
            // Execute the insert statement
            statement.executeUpdate();
        }
    }

    public void userSignUp(String username, String password, String name, String email, int age, String city, String state, int zipcode) throws SQLException {
        String sql = "INSERT INTO ums_user_login (username,password,name, email, age, city, state, zipcode) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";

        try (PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setString(1, username);
            statement.setString(2, password);
            statement.setString(3, name);
            statement.setString(4, email);
            statement.setInt(5, age);
            statement.setString(6, city);
            statement.setString(7, state);
            statement.setInt(8, zipcode);
            // Execute the insert statement
            statement.executeUpdate();
        }
    }
    
    public void adminModify(String username, String password, String name, String email, int age, String city, String state, int zipcode) throws SQLException {
        String sql = "UPDATE ums_admin_login SET password=?, name=?, email=?, age=?, city=?, state=?, zipcode=? WHERE username=?";

        try (PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setString(1, password);
            statement.setString(2, name);
            statement.setString(3, email);
            statement.setInt(4, age);
            statement.setString(5, city);
            statement.setString(6, state);
            statement.setInt(7, zipcode);
            statement.setString(8, username);
            
            // Execute the update statement
            statement.executeUpdate();
        }
    }
    
    public void userModify(String username, String password, String name, String email, int age, String city, String state, int zipcode) throws SQLException {
        String sql = "UPDATE ums_user_login SET password=?, name=?, email=?, age=?, city=?, state=?, zipcode=? WHERE username=?";

        try (PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setString(1, password);
            statement.setString(2, name);
            statement.setString(3, email);
            statement.setInt(4, age);
            statement.setString(5, city);
            statement.setString(6, state);
            statement.setInt(7, zipcode);
            statement.setString(8, username);
            
            // Execute the update statement
            statement.executeUpdate();
        }
    }
    
	
    public ObservableList<ManageUtilityIncident> getGeneratedIncidents() {
        ObservableList<ManageUtilityIncident> incidents = FXCollections.observableArrayList();
        String sql = "SELECT * FROM ums_user_incident WHERE generate_incident = 'yes'";

        try (PreparedStatement statement = connection.prepareStatement(sql)) {
            try (ResultSet resultSet = statement.executeQuery()) {
                while (resultSet.next()) {
                    // Retrieve data from the result set (similar to the previous method)
                    int customerId = resultSet.getInt("customerid");
                    String utilityType = resultSet.getString("utility_type");
                    String incidentStatus = resultSet.getString("incident_status");
                    String incidentDescription = resultSet.getString("incident_description");
                    String generateIncident = resultSet.getString("generate_incident");

                    ManageUtilityIncident incident = new ManageUtilityIncident(customerId, utilityType, incidentStatus, incidentDescription, generateIncident);
                    incidents.add(incident);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
            System.out.println("Error fetching generated incidents: " + e.getMessage());
        }

        return incidents;
    }

	 

	/*
	 * public ObservableList<ManageUtilityIncident> getGeneratedIncidents() {
	 * ObservableList<ManageUtilityIncident> incidents =
	 * FXCollections.observableArrayList(); String sql =
	 * "SELECT * FROM ums_user_incident WHERE generate_incident = 'yes'";
	 * 
	 * try (PreparedStatement statement = connection.prepareStatement(sql)) {
	 * ResultSet resultSet = statement.executeQuery(); while (resultSet.next()) { //
	 * Retrieve data from the result set (similar to the previous method) int
	 * customerId = resultSet.getInt("customerid"); String utilityType =
	 * resultSet.getString("utility_type"); String incidentStatus =
	 * resultSet.getString("incident_status"); String incidentDescription =
	 * resultSet.getString("incident_description"); String generateIncident =
	 * resultSet.getString("generate_incident");
	 * 
	 * ManageUtilityIncident incident = new ManageUtilityIncident(customerId,
	 * utilityType, incidentStatus, incidentDescription, generateIncident);
	 * incidents.add(incident);
	 * 
	 * //System.out.println("Fetched incident: " + incident); } } catch
	 * (SQLException e) { e.printStackTrace();
	 * System.out.println("Error fetching generated incidents: " + e.getMessage());
	 * }
	 * 
	 * return incidents; }
	 */

    
    public ObservableList<ManageUtilityIncident> searchIncident(int customerId) {
        ObservableList<ManageUtilityIncident> incidents = FXCollections.observableArrayList();
        String sql = "SELECT * FROM ums_user_incident WHERE customerid = ?";

        try (PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setInt(1, customerId);
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                // Retrieve data from the result set (similar to the previous method)
                int retrievedCustomerId = resultSet.getInt("customerid");
                String utilityType = resultSet.getString("utility_type");
                String incidentStatus = resultSet.getString("incident_status");
                String incidentDescription = resultSet.getString("incident_description");
                String generateIncident = resultSet.getString("generate_incident");

                ManageUtilityIncident incident = new ManageUtilityIncident(retrievedCustomerId, utilityType, incidentStatus, incidentDescription, generateIncident);
                incidents.add(incident);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return incidents;
    }

    public void resolveIncident(int customerId) {
        String sql = "UPDATE ums_user_incident SET incident_status = 'resolved', generate_incident = 'none' WHERE customerid = ?";

        try (PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setInt(1, customerId);
            statement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

}
