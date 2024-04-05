package controllers;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.effect.DropShadow;
import javafx.stage.Stage;

public class AdminHomeController {

    @FXML
    private ImageView imgbtn_ManageUtility;

    @FXML
    private ImageView imgbtn_AdminHomelogout;

    @FXML
    private ImageView imgbtn_ManageProfiles;

    //private Stage adminStage;

    @FXML
    public void initialize() {
		
		// Add event handlers
    	imgbtn_ManageUtility.setOnMouseClicked(event -> handleManageUtility(event));
    	imgbtn_ManageUtility.setOnMouseEntered(event -> handleMouseEnter(event));
    	imgbtn_ManageUtility.setOnMouseExited(event -> handleMouseExit(event));

    	imgbtn_ManageProfiles.setOnMouseClicked(event -> handleManageProfiles(event));
    	imgbtn_ManageProfiles.setOnMouseEntered(event -> handleMouseEnter(event));
    	imgbtn_ManageProfiles.setOnMouseExited(event -> handleMouseExit(event));

	    imgbtn_AdminHomelogout.setOnMouseClicked(event -> handleAdminHomelogout(event));
	    imgbtn_AdminHomelogout.setOnMouseEntered(event -> handleMouseEnter(event));
	    imgbtn_AdminHomelogout.setOnMouseExited(event -> handleMouseExit(event));
	    }

    private void handleMouseEnter(MouseEvent event) {
        ImageView source = (ImageView) event.getSource();
        DropShadow dropShadow = new DropShadow();
        source.setEffect(dropShadow);
    }

    private void handleMouseExit(MouseEvent event) {
        ImageView source = (ImageView) event.getSource();
        source.setEffect(null);
    }
    
    @FXML
    void handleManageUtility(MouseEvent event) {
        highlightImage(imgbtn_ManageUtility);
        // Add your logic for "Manage Utility" here
        loadFXML("ManageUtilityIncident.fxml");
    }

	@FXML
    void handleAdminHomelogout(MouseEvent event) {
        highlightImage(imgbtn_AdminHomelogout);
        // Add your logic for "Logout" here
        closeStage();
       }

	@FXML
    void handleManageProfiles(MouseEvent event) {
        highlightImage(imgbtn_ManageProfiles);
        // Add your logic for "Manage Profiles" here
        loadFXML("ManageAdminProfile.fxml");
        }

    private void highlightImage(ImageView image) {
        // Highlight the image when the mouse hovers over it
        image.setStyle("-fx-effect: dropshadow(three-pass-box, rgba(255,255,255,0.8), 10, 0, 0, 0);");
    }

    private void loadFXML(String fxmlFileName) {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource(fxmlFileName));
            Parent root = loader.load();
            Stage stage = new Stage();
            stage.setScene(new Scene(root));
            stage.setTitle("Your Title"); // Set the title as needed
            stage.show();
        } catch (IOException e) {
            e.printStackTrace();
            showAlert("Error", "Error loading the scene.");
        }
    }
    
    private void closeStage() {
        // Close the current admin stage
        Stage adminStage = (Stage) imgbtn_AdminHomelogout.getScene().getWindow();
        adminStage.close();
    }
    
    private void showAlert(String title, String content) {
        Alert alert = new Alert(AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setContentText(content);
        alert.showAndWait();
    }

	public void setSceneController(SceneController sceneController) {
		// TODO Auto-generated method stub
		
	}
}
