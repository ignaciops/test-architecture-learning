import pytest
import allure

@allure.epic("API Tests")
@allure.feature("Badges Awarding")
@allure.story("Awarding Bronce Badge to User")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
def test_user_receives_bronce_badge_after_attending_1_event(badge_awarding_scenario):
  """
  Test that a user receives a bronze badge after attending 1 event.
  """

   # Arrange & Act
  badge_awarding = badge_awarding_scenario
  with allure.step("Crear un usuario y registrar su asistencia a 1 evento"):
    user_data = {"username": "test_user_bronze", "discord_id": "1234567889"}
    user_id = badge_awarding.create_user_with_attendances(user_data, event_ids=[1])

    allure.attach(
      f"User ID: {user_id}",
      name="User Created",
      attachment_type=allure.attachment_type.TEXT
    )

  with allure.step("Verificar que el usuario recibió la insignia de bronce"):
    user_has_bronze_badge = badge_awarding.user_has_badge(user_id, "Bronce")
    assert user_has_bronze_badge, "El usuario no recibió el badge Bronce"

@allure.epic("API Tests")
@allure.feature("Badges Awarding")
@allure.story("Awarding Plata Badge to User")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
def test_user_receives_plata_badge_after_attending_5_events(badge_awarding_scenario):
  """
  Test that a user receives a plata badge after attending 5 events.
  """

   # Arrange & Act
  badge_awarding = badge_awarding_scenario
  with allure.step("Crear un usuario y registrar su asistencia a 5 eventos"):
    user_data = {"username": "test_user_plata", "discord_id": "13243546576879"}
    user_id = badge_awarding.create_user_with_attendances(user_data, event_ids=[1, 2, 3, 4, 5])

    allure.attach(
      f"User ID: {user_id}",
      name="User Created",
      attachment_type=allure.attachment_type.TEXT
    )

  with allure.step("Verificar que el usuario recibió la insignia de plata"):
    user_has_plata_badge = badge_awarding.user_has_badge(user_id, "Plata")
    assert user_has_plata_badge, "El usuario no recibió el badge Plata"

@allure.epic("API Tests")
@allure.feature("Badges Awarding")
@allure.story("Awarding Oro Badge to User")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
def test_user_receives_oro_badge_after_attending_10_events(badge_awarding_scenario, gold_badge_created):
  """
  Test that a user receives an oro badge after attending 10 events.
  """

   # Arrange & Act
  badge_awarding = badge_awarding_scenario
  with allure.step("Crear un usuario y registrar su asistencia a 10 eventos"):
    user_data = {"username": "test_user_oro", "discord_id": "12345678901234"}
    user_id = badge_awarding.create_user_with_attendances(user_data, event_ids=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    allure.attach(
      f"User ID: {user_id}",
      name="User Created",
      attachment_type=allure.attachment_type.TEXT
    )

  with allure.step("Verificar que el usuario recibió la insignia de oro"):
    user_has_oro_badge = badge_awarding.user_has_badge(user_id, "Oro")
    assert user_has_oro_badge, "El usuario no recibió el badge Oro"

@allure.epic("API Tests")
@allure.feature("Badges Awarding")
@allure.story("Idempotency of Attendance Registration")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
def test_idempotency_of_attendance_registration(badge_awarding_scenario):
  """
  Test that registering the same attendance multiple times does not affect badge awarding.
  """

   # Arrange & Act
  badge_awarding = badge_awarding_scenario
  with allure.step("Crear un usuario"):
    user_data = {"username": "test_user_idempotent", "discord_id": "98765432106784"}
    user_id = badge_awarding.create_user_with_attendances(user_data, event_ids=[1, 2, 3, 4])

    allure.attach(
      f"User ID: {user_id}",
      name="User Created",
      attachment_type=allure.attachment_type.TEXT
    )
  with allure.step("Registrar la misma asistencia una vez más"):
    attendance = badge_awarding.register_attendance(user_id, event_id=1)
    allure.attach(
      f"Attendance Response: {attendance.status_code}",
      name="Attendance Registered Again",
      attachment_type=allure.attachment_type.TEXT
    )

  with allure.step("Verificar que el status code de la respuesta es 409"):
    assert attendance.status_code == 409, f"La respuesta no es 409, respuesta: {attendance.status_code}"

  with allure.step("Verificar que el usuario aún tiene la insignia de bronce y no recibió la de plata"):
    has_bronze_badge = badge_awarding.user_has_badge(user_id, "Bronce")
    has_plata_badge = badge_awarding.user_has_badge(user_id, "Plata")
    assert has_bronze_badge, "El usuario no tiene la insignia de bronce"
    assert not has_plata_badge, "El usuario no debería tener la insignia de plata"