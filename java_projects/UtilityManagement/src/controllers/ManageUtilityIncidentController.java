package controllers;

import java.io.IOException;

import dao.DBConnect;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import models.ManageUtilityIncident;
import javafx.scene.Node;

public class ManageUtilityIncidentController {

    @FXML
    private TextField txtCustomerID;

    @FXML
    private Button btnBack;

    @FXML
    private Button btnSearch;

    @FXML
    private Button btnResolve;

    @FXML
    private Button btnSearchIncident;

    @FXML
    private TableView<ManageUtilityIncident> incidentTable;

    DBConnect dbConnect = new DBConnect();

    public static void setAdminHomeStage(Stage stage) {
    }
    
   
    @FXML
    public void handleBackButton(ActionEvent event) {
        Object adminLoginStage = null;
		if (adminLoginStage != null) {
            // If AdminLogin stage is not null, bring it to the front
            ((Node) adminLoginStage).toFront();
        } else {
            // If AdminLogin stage is null, open a new instance
            openAdminHomePage(event);
        }

        // Close the current AdminSignUp stage
        Stage adminHomeStage = (Stage) btnBack.getScene().getWindow();
        adminHomeStage.close();
    }


    private void openAdminHomePage(ActionEvent event) {
		// TODO Auto-generated method stub
		
	}

	@FXML
    public void handleSearchButton(ActionEvent event) {
        // Get the customer ID from the TextField
        int customerId = Integer.parseInt(txtCustomerID.getText());

        // Call a method in DBConnect to retrieve the incident with the specified customer ID
        ObservableList<ManageUtilityIncident> incidents = dbConnect.searchIncident(customerId);

        // Populate the TableView with the retrieved incident
        populateIncidentTable(incidents);
    }

    @FXML
    public void handleResolveButton(ActionEvent event) {
        // Get the selected incident from the TableView
        ManageUtilityIncident selectedIncident = incidentTable.getSelectionModel().getSelectedItem();

        if (selectedIncident != null) {
            // Call a method in DBConnect to update the incident status to resolved
            dbConnect.resolveIncident(selectedIncident.getCustomerId());

            // Refresh the TableView
            handleSearchIncidentButton(event);
        } else {
            // Show an alert or message indicating that no incident is selected
            showAlert("No Incident Selected", "Please select an incident from the table.");
        }
    }

    @FXML
    public void handleSearchIncidentButton(ActionEvent event) {
        // Call a method in DBConnect to retrieve incidents with "generate incident" = yes
        ObservableList<ManageUtilityIncident> incidents = dbConnect.getGeneratedIncidents();

        // Populate the TableView with the retrieved incidents
        populateIncidentTable(incidents);
    }

    private void populateIncidentTable(ObservableList<ManageUtilityIncident> incidents) {
        // Clear existing items
        incidentTable.getItems().clear();
        // Add new items
        incidentTable.getItems().addAll(incidents);
    }

    private void showAlert(String title, String content) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setContentText(content);
        alert.showAndWait();
    }
}
