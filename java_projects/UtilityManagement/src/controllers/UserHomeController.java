package controllers;

import java.io.IOException;

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

public class UserHomeController {

    @FXML
    private ImageView imgbtn_Electricity;

    @FXML
    private ImageView imgbtn_UserHomelogout;

    @FXML
    private ImageView imgbtn_water;

    @FXML
    private ImageView imgbtn_gas;

    @FXML
    private ImageView imgbtn_UserManageProfile;

    //private Stage userStage;

    @FXML
    public void initialize() {
        // Add event handlers
        imgbtn_Electricity.setOnMouseClicked(event -> handleManageElectricity(event));
        imgbtn_Electricity.setOnMouseEntered(event -> handleMouseEnter(event));
        imgbtn_Electricity.setOnMouseExited(event -> handleMouseExit(event));

        imgbtn_water.setOnMouseClicked(event -> handleManageWater(event));
        imgbtn_water.setOnMouseEntered(event -> handleMouseEnter(event));
        imgbtn_water.setOnMouseExited(event -> handleMouseExit(event));

        imgbtn_gas.setOnMouseClicked(event -> handleManageGas(event));
        imgbtn_gas.setOnMouseEntered(event -> handleMouseEnter(event));
        imgbtn_gas.setOnMouseExited(event -> handleMouseExit(event));

        imgbtn_UserHomelogout.setOnMouseClicked(event -> handleUserHomelogout(event));
        imgbtn_UserHomelogout.setOnMouseEntered(event -> handleMouseEnter(event));
        imgbtn_UserHomelogout.setOnMouseExited(event -> handleMouseExit(event));

        imgbtn_UserManageProfile.setOnMouseClicked(event -> handleUserManageProfile(event));
        imgbtn_UserManageProfile.setOnMouseEntered(event -> handleMouseEnter(event));
        imgbtn_UserManageProfile.setOnMouseExited(event -> handleMouseExit(event));
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
    void handleManageElectricity(MouseEvent event) {
        highlightImage(imgbtn_Electricity);
        showAlert("Option Selected", "Manage Electricity Selected");
        // Add logic to open the corresponding scene or perform actions
    }

	@FXML
    void handleManageWater(MouseEvent event) {
        highlightImage(imgbtn_water);
        showAlert("Option Selected", "Manage Water Selected");
        // Add logic to open the corresponding scene or perform actions
    }

    @FXML
    void handleManageGas(MouseEvent event) {
        highlightImage(imgbtn_gas);
        showAlert("Option Selected", "Manage Gas Selected");
        // Add logic to open the corresponding scene or perform actions
    }

    @FXML
    void handleUserHomelogout(MouseEvent event) {
        highlightImage(imgbtn_UserHomelogout);
        closeStage();
        // Add logic to perform logout actions
    }


	@FXML
    void handleUserManageProfile(MouseEvent event) {
        highlightImage(imgbtn_UserManageProfile);
        loadFXML("ManageUserProfile.fxml");
    }
        // Add logic to open the corresponding scene or perform actions
    

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
        Stage adminStage = (Stage) imgbtn_UserHomelogout.getScene().getWindow();
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
		
	}}

