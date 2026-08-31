from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_delivery_controllers_update_annotations_error_component import (
        ApiV1DeliveryControllersUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_applications_degraded_error_component import (
        ApiV1DeliveryControllersUpdateApplicationsDegradedErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_applications_out_of_sync_error_component import (
        ApiV1DeliveryControllersUpdateApplicationsOutOfSyncErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_applications_synced_error_component import (
        ApiV1DeliveryControllersUpdateApplicationsSyncedErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_applications_total_error_component import (
        ApiV1DeliveryControllersUpdateApplicationsTotalErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_archived_at_error_component import (
        ApiV1DeliveryControllersUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_archived_error_component import (
        ApiV1DeliveryControllersUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_archived_reason_error_component import (
        ApiV1DeliveryControllersUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_controller_app_version_error_component import (
        ApiV1DeliveryControllersUpdateControllerAppVersionErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_credential_error_component import (
        ApiV1DeliveryControllersUpdateCredentialErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_criticality_error_component import (
        ApiV1DeliveryControllersUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_debug_mode_error_component import (
        ApiV1DeliveryControllersUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_display_name_error_component import (
        ApiV1DeliveryControllersUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_hostname_error_component import (
        ApiV1DeliveryControllersUpdateHostnameErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_k8s_app_error_component import (
        ApiV1DeliveryControllersUpdateK8SAppErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_k8s_cluster_error_component import (
        ApiV1DeliveryControllersUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_kind_error_component import (
        ApiV1DeliveryControllersUpdateKindErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_labels_error_component import (
        ApiV1DeliveryControllersUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_metadata_error_component import (
        ApiV1DeliveryControllersUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_name_error_component import (
        ApiV1DeliveryControllersUpdateNameErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_non_field_errors_error_component import (
        ApiV1DeliveryControllersUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_platform_service_error_component import (
        ApiV1DeliveryControllersUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_provider_error_component import (
        ApiV1DeliveryControllersUpdateProviderErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_provider_id_error_component import (
        ApiV1DeliveryControllersUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_provider_reference_error_component import (
        ApiV1DeliveryControllersUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_reconciliation_enabled_error_component import (
        ApiV1DeliveryControllersUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_sla_availability_error_component import (
        ApiV1DeliveryControllersUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_sla_target_error_component import (
        ApiV1DeliveryControllersUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_slo_availability_error_component import (
        ApiV1DeliveryControllersUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_slo_target_error_component import (
        ApiV1DeliveryControllersUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_target_availability_error_component import (
        ApiV1DeliveryControllersUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_update_tolerations_error_component import (
        ApiV1DeliveryControllersUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DeliveryControllersUpdateValidationError")


@_attrs_define
class ApiV1DeliveryControllersUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DeliveryControllersUpdateAnnotationsErrorComponent |
            ApiV1DeliveryControllersUpdateApplicationsDegradedErrorComponent |
            ApiV1DeliveryControllersUpdateApplicationsOutOfSyncErrorComponent |
            ApiV1DeliveryControllersUpdateApplicationsSyncedErrorComponent |
            ApiV1DeliveryControllersUpdateApplicationsTotalErrorComponent |
            ApiV1DeliveryControllersUpdateArchivedAtErrorComponent | ApiV1DeliveryControllersUpdateArchivedErrorComponent |
            ApiV1DeliveryControllersUpdateArchivedReasonErrorComponent |
            ApiV1DeliveryControllersUpdateControllerAppVersionErrorComponent |
            ApiV1DeliveryControllersUpdateCredentialErrorComponent | ApiV1DeliveryControllersUpdateCriticalityErrorComponent
            | ApiV1DeliveryControllersUpdateDebugModeErrorComponent |
            ApiV1DeliveryControllersUpdateDisplayNameErrorComponent | ApiV1DeliveryControllersUpdateHostnameErrorComponent |
            ApiV1DeliveryControllersUpdateK8SAppErrorComponent | ApiV1DeliveryControllersUpdateK8SClusterErrorComponent |
            ApiV1DeliveryControllersUpdateKindErrorComponent | ApiV1DeliveryControllersUpdateLabelsErrorComponent |
            ApiV1DeliveryControllersUpdateMetadataErrorComponent | ApiV1DeliveryControllersUpdateNameErrorComponent |
            ApiV1DeliveryControllersUpdateNonFieldErrorsErrorComponent |
            ApiV1DeliveryControllersUpdatePlatformServiceErrorComponent |
            ApiV1DeliveryControllersUpdateProviderErrorComponent | ApiV1DeliveryControllersUpdateProviderIdErrorComponent |
            ApiV1DeliveryControllersUpdateProviderReferenceErrorComponent |
            ApiV1DeliveryControllersUpdateReconciliationEnabledErrorComponent |
            ApiV1DeliveryControllersUpdateSlaAvailabilityErrorComponent |
            ApiV1DeliveryControllersUpdateSlaTargetErrorComponent |
            ApiV1DeliveryControllersUpdateSloAvailabilityErrorComponent |
            ApiV1DeliveryControllersUpdateSloTargetErrorComponent |
            ApiV1DeliveryControllersUpdateTargetAvailabilityErrorComponent |
            ApiV1DeliveryControllersUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DeliveryControllersUpdateAnnotationsErrorComponent
        | ApiV1DeliveryControllersUpdateApplicationsDegradedErrorComponent
        | ApiV1DeliveryControllersUpdateApplicationsOutOfSyncErrorComponent
        | ApiV1DeliveryControllersUpdateApplicationsSyncedErrorComponent
        | ApiV1DeliveryControllersUpdateApplicationsTotalErrorComponent
        | ApiV1DeliveryControllersUpdateArchivedAtErrorComponent
        | ApiV1DeliveryControllersUpdateArchivedErrorComponent
        | ApiV1DeliveryControllersUpdateArchivedReasonErrorComponent
        | ApiV1DeliveryControllersUpdateControllerAppVersionErrorComponent
        | ApiV1DeliveryControllersUpdateCredentialErrorComponent
        | ApiV1DeliveryControllersUpdateCriticalityErrorComponent
        | ApiV1DeliveryControllersUpdateDebugModeErrorComponent
        | ApiV1DeliveryControllersUpdateDisplayNameErrorComponent
        | ApiV1DeliveryControllersUpdateHostnameErrorComponent
        | ApiV1DeliveryControllersUpdateK8SAppErrorComponent
        | ApiV1DeliveryControllersUpdateK8SClusterErrorComponent
        | ApiV1DeliveryControllersUpdateKindErrorComponent
        | ApiV1DeliveryControllersUpdateLabelsErrorComponent
        | ApiV1DeliveryControllersUpdateMetadataErrorComponent
        | ApiV1DeliveryControllersUpdateNameErrorComponent
        | ApiV1DeliveryControllersUpdateNonFieldErrorsErrorComponent
        | ApiV1DeliveryControllersUpdatePlatformServiceErrorComponent
        | ApiV1DeliveryControllersUpdateProviderErrorComponent
        | ApiV1DeliveryControllersUpdateProviderIdErrorComponent
        | ApiV1DeliveryControllersUpdateProviderReferenceErrorComponent
        | ApiV1DeliveryControllersUpdateReconciliationEnabledErrorComponent
        | ApiV1DeliveryControllersUpdateSlaAvailabilityErrorComponent
        | ApiV1DeliveryControllersUpdateSlaTargetErrorComponent
        | ApiV1DeliveryControllersUpdateSloAvailabilityErrorComponent
        | ApiV1DeliveryControllersUpdateSloTargetErrorComponent
        | ApiV1DeliveryControllersUpdateTargetAvailabilityErrorComponent
        | ApiV1DeliveryControllersUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_delivery_controllers_update_annotations_error_component import (
            ApiV1DeliveryControllersUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_applications_degraded_error_component import (
            ApiV1DeliveryControllersUpdateApplicationsDegradedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_applications_out_of_sync_error_component import (
            ApiV1DeliveryControllersUpdateApplicationsOutOfSyncErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_applications_synced_error_component import (
            ApiV1DeliveryControllersUpdateApplicationsSyncedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_applications_total_error_component import (
            ApiV1DeliveryControllersUpdateApplicationsTotalErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_archived_at_error_component import (
            ApiV1DeliveryControllersUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_archived_error_component import (
            ApiV1DeliveryControllersUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_archived_reason_error_component import (
            ApiV1DeliveryControllersUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_controller_app_version_error_component import (
            ApiV1DeliveryControllersUpdateControllerAppVersionErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_credential_error_component import (
            ApiV1DeliveryControllersUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_criticality_error_component import (
            ApiV1DeliveryControllersUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_debug_mode_error_component import (
            ApiV1DeliveryControllersUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_display_name_error_component import (
            ApiV1DeliveryControllersUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_hostname_error_component import (
            ApiV1DeliveryControllersUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_k8s_app_error_component import (
            ApiV1DeliveryControllersUpdateK8SAppErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_k8s_cluster_error_component import (
            ApiV1DeliveryControllersUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_kind_error_component import (
            ApiV1DeliveryControllersUpdateKindErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_labels_error_component import (
            ApiV1DeliveryControllersUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_name_error_component import (
            ApiV1DeliveryControllersUpdateNameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_non_field_errors_error_component import (
            ApiV1DeliveryControllersUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_platform_service_error_component import (
            ApiV1DeliveryControllersUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_provider_error_component import (
            ApiV1DeliveryControllersUpdateProviderErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_provider_id_error_component import (
            ApiV1DeliveryControllersUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_provider_reference_error_component import (
            ApiV1DeliveryControllersUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_reconciliation_enabled_error_component import (
            ApiV1DeliveryControllersUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_sla_availability_error_component import (
            ApiV1DeliveryControllersUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_sla_target_error_component import (
            ApiV1DeliveryControllersUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_slo_availability_error_component import (
            ApiV1DeliveryControllersUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_slo_target_error_component import (
            ApiV1DeliveryControllersUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_target_availability_error_component import (
            ApiV1DeliveryControllersUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_tolerations_error_component import (
            ApiV1DeliveryControllersUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DeliveryControllersUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateApplicationsTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateApplicationsSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateApplicationsOutOfSyncErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateApplicationsDegradedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateControllerAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersUpdateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_delivery_controllers_update_annotations_error_component import (
            ApiV1DeliveryControllersUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_applications_degraded_error_component import (
            ApiV1DeliveryControllersUpdateApplicationsDegradedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_applications_out_of_sync_error_component import (
            ApiV1DeliveryControllersUpdateApplicationsOutOfSyncErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_applications_synced_error_component import (
            ApiV1DeliveryControllersUpdateApplicationsSyncedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_applications_total_error_component import (
            ApiV1DeliveryControllersUpdateApplicationsTotalErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_archived_at_error_component import (
            ApiV1DeliveryControllersUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_archived_error_component import (
            ApiV1DeliveryControllersUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_archived_reason_error_component import (
            ApiV1DeliveryControllersUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_controller_app_version_error_component import (
            ApiV1DeliveryControllersUpdateControllerAppVersionErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_credential_error_component import (
            ApiV1DeliveryControllersUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_criticality_error_component import (
            ApiV1DeliveryControllersUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_debug_mode_error_component import (
            ApiV1DeliveryControllersUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_display_name_error_component import (
            ApiV1DeliveryControllersUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_hostname_error_component import (
            ApiV1DeliveryControllersUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_k8s_app_error_component import (
            ApiV1DeliveryControllersUpdateK8SAppErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_k8s_cluster_error_component import (
            ApiV1DeliveryControllersUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_kind_error_component import (
            ApiV1DeliveryControllersUpdateKindErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_labels_error_component import (
            ApiV1DeliveryControllersUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_metadata_error_component import (
            ApiV1DeliveryControllersUpdateMetadataErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_name_error_component import (
            ApiV1DeliveryControllersUpdateNameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_non_field_errors_error_component import (
            ApiV1DeliveryControllersUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_platform_service_error_component import (
            ApiV1DeliveryControllersUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_provider_error_component import (
            ApiV1DeliveryControllersUpdateProviderErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_provider_id_error_component import (
            ApiV1DeliveryControllersUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_provider_reference_error_component import (
            ApiV1DeliveryControllersUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_reconciliation_enabled_error_component import (
            ApiV1DeliveryControllersUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_sla_availability_error_component import (
            ApiV1DeliveryControllersUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_sla_target_error_component import (
            ApiV1DeliveryControllersUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_slo_availability_error_component import (
            ApiV1DeliveryControllersUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_slo_target_error_component import (
            ApiV1DeliveryControllersUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_target_availability_error_component import (
            ApiV1DeliveryControllersUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_update_tolerations_error_component import (
            ApiV1DeliveryControllersUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DeliveryControllersUpdateAnnotationsErrorComponent
                | ApiV1DeliveryControllersUpdateApplicationsDegradedErrorComponent
                | ApiV1DeliveryControllersUpdateApplicationsOutOfSyncErrorComponent
                | ApiV1DeliveryControllersUpdateApplicationsSyncedErrorComponent
                | ApiV1DeliveryControllersUpdateApplicationsTotalErrorComponent
                | ApiV1DeliveryControllersUpdateArchivedAtErrorComponent
                | ApiV1DeliveryControllersUpdateArchivedErrorComponent
                | ApiV1DeliveryControllersUpdateArchivedReasonErrorComponent
                | ApiV1DeliveryControllersUpdateControllerAppVersionErrorComponent
                | ApiV1DeliveryControllersUpdateCredentialErrorComponent
                | ApiV1DeliveryControllersUpdateCriticalityErrorComponent
                | ApiV1DeliveryControllersUpdateDebugModeErrorComponent
                | ApiV1DeliveryControllersUpdateDisplayNameErrorComponent
                | ApiV1DeliveryControllersUpdateHostnameErrorComponent
                | ApiV1DeliveryControllersUpdateK8SAppErrorComponent
                | ApiV1DeliveryControllersUpdateK8SClusterErrorComponent
                | ApiV1DeliveryControllersUpdateKindErrorComponent
                | ApiV1DeliveryControllersUpdateLabelsErrorComponent
                | ApiV1DeliveryControllersUpdateMetadataErrorComponent
                | ApiV1DeliveryControllersUpdateNameErrorComponent
                | ApiV1DeliveryControllersUpdateNonFieldErrorsErrorComponent
                | ApiV1DeliveryControllersUpdatePlatformServiceErrorComponent
                | ApiV1DeliveryControllersUpdateProviderErrorComponent
                | ApiV1DeliveryControllersUpdateProviderIdErrorComponent
                | ApiV1DeliveryControllersUpdateProviderReferenceErrorComponent
                | ApiV1DeliveryControllersUpdateReconciliationEnabledErrorComponent
                | ApiV1DeliveryControllersUpdateSlaAvailabilityErrorComponent
                | ApiV1DeliveryControllersUpdateSlaTargetErrorComponent
                | ApiV1DeliveryControllersUpdateSloAvailabilityErrorComponent
                | ApiV1DeliveryControllersUpdateSloTargetErrorComponent
                | ApiV1DeliveryControllersUpdateTargetAvailabilityErrorComponent
                | ApiV1DeliveryControllersUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_0 = (
                        ApiV1DeliveryControllersUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_1 = (
                        ApiV1DeliveryControllersUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_2 = (
                        ApiV1DeliveryControllersUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_3 = (
                        ApiV1DeliveryControllersUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_4 = (
                        ApiV1DeliveryControllersUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_5 = (
                        ApiV1DeliveryControllersUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_6 = (
                        ApiV1DeliveryControllersUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_7 = (
                        ApiV1DeliveryControllersUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_8 = (
                        ApiV1DeliveryControllersUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_9 = (
                        ApiV1DeliveryControllersUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_10 = (
                        ApiV1DeliveryControllersUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_11 = (
                        ApiV1DeliveryControllersUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_12 = (
                        ApiV1DeliveryControllersUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_13 = (
                        ApiV1DeliveryControllersUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_14 = (
                        ApiV1DeliveryControllersUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_15 = (
                        ApiV1DeliveryControllersUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_16 = (
                        ApiV1DeliveryControllersUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_17 = (
                        ApiV1DeliveryControllersUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_18 = (
                        ApiV1DeliveryControllersUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_19 = (
                        ApiV1DeliveryControllersUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_20 = (
                        ApiV1DeliveryControllersUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_21 = (
                        ApiV1DeliveryControllersUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_22 = (
                        ApiV1DeliveryControllersUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_23 = (
                        ApiV1DeliveryControllersUpdateApplicationsTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_24 = (
                        ApiV1DeliveryControllersUpdateApplicationsSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_25 = (
                        ApiV1DeliveryControllersUpdateApplicationsOutOfSyncErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_26 = (
                        ApiV1DeliveryControllersUpdateApplicationsDegradedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_27 = (
                        ApiV1DeliveryControllersUpdateControllerAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_28 = (
                        ApiV1DeliveryControllersUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_29 = (
                        ApiV1DeliveryControllersUpdateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_update_error_type_30 = (
                        ApiV1DeliveryControllersUpdateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_delivery_controllers_update_error_type_31 = (
                    ApiV1DeliveryControllersUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_delivery_controllers_update_error_type_31

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_delivery_controllers_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_delivery_controllers_update_validation_error.additional_properties = d
        return api_v1_delivery_controllers_update_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
