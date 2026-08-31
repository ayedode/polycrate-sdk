from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_delivery_controllers_partial_update_annotations_error_component import (
        ApiV1DeliveryControllersPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_applications_degraded_error_component import (
        ApiV1DeliveryControllersPartialUpdateApplicationsDegradedErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_applications_out_of_sync_error_component import (
        ApiV1DeliveryControllersPartialUpdateApplicationsOutOfSyncErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_applications_synced_error_component import (
        ApiV1DeliveryControllersPartialUpdateApplicationsSyncedErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_applications_total_error_component import (
        ApiV1DeliveryControllersPartialUpdateApplicationsTotalErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_archived_at_error_component import (
        ApiV1DeliveryControllersPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_archived_error_component import (
        ApiV1DeliveryControllersPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_archived_reason_error_component import (
        ApiV1DeliveryControllersPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_controller_app_version_error_component import (
        ApiV1DeliveryControllersPartialUpdateControllerAppVersionErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_credential_error_component import (
        ApiV1DeliveryControllersPartialUpdateCredentialErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_criticality_error_component import (
        ApiV1DeliveryControllersPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_debug_mode_error_component import (
        ApiV1DeliveryControllersPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_display_name_error_component import (
        ApiV1DeliveryControllersPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_hostname_error_component import (
        ApiV1DeliveryControllersPartialUpdateHostnameErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_k8s_app_error_component import (
        ApiV1DeliveryControllersPartialUpdateK8SAppErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_k8s_cluster_error_component import (
        ApiV1DeliveryControllersPartialUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_kind_error_component import (
        ApiV1DeliveryControllersPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_labels_error_component import (
        ApiV1DeliveryControllersPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_metadata_error_component import (
        ApiV1DeliveryControllersPartialUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_name_error_component import (
        ApiV1DeliveryControllersPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_non_field_errors_error_component import (
        ApiV1DeliveryControllersPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_platform_service_error_component import (
        ApiV1DeliveryControllersPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_provider_error_component import (
        ApiV1DeliveryControllersPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_provider_id_error_component import (
        ApiV1DeliveryControllersPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_provider_reference_error_component import (
        ApiV1DeliveryControllersPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_reconciliation_enabled_error_component import (
        ApiV1DeliveryControllersPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_sla_availability_error_component import (
        ApiV1DeliveryControllersPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_sla_target_error_component import (
        ApiV1DeliveryControllersPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_slo_availability_error_component import (
        ApiV1DeliveryControllersPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_slo_target_error_component import (
        ApiV1DeliveryControllersPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_target_availability_error_component import (
        ApiV1DeliveryControllersPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_partial_update_tolerations_error_component import (
        ApiV1DeliveryControllersPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DeliveryControllersPartialUpdateValidationError")


@_attrs_define
class ApiV1DeliveryControllersPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DeliveryControllersPartialUpdateAnnotationsErrorComponent |
            ApiV1DeliveryControllersPartialUpdateApplicationsDegradedErrorComponent |
            ApiV1DeliveryControllersPartialUpdateApplicationsOutOfSyncErrorComponent |
            ApiV1DeliveryControllersPartialUpdateApplicationsSyncedErrorComponent |
            ApiV1DeliveryControllersPartialUpdateApplicationsTotalErrorComponent |
            ApiV1DeliveryControllersPartialUpdateArchivedAtErrorComponent |
            ApiV1DeliveryControllersPartialUpdateArchivedErrorComponent |
            ApiV1DeliveryControllersPartialUpdateArchivedReasonErrorComponent |
            ApiV1DeliveryControllersPartialUpdateControllerAppVersionErrorComponent |
            ApiV1DeliveryControllersPartialUpdateCredentialErrorComponent |
            ApiV1DeliveryControllersPartialUpdateCriticalityErrorComponent |
            ApiV1DeliveryControllersPartialUpdateDebugModeErrorComponent |
            ApiV1DeliveryControllersPartialUpdateDisplayNameErrorComponent |
            ApiV1DeliveryControllersPartialUpdateHostnameErrorComponent |
            ApiV1DeliveryControllersPartialUpdateK8SAppErrorComponent |
            ApiV1DeliveryControllersPartialUpdateK8SClusterErrorComponent |
            ApiV1DeliveryControllersPartialUpdateKindErrorComponent |
            ApiV1DeliveryControllersPartialUpdateLabelsErrorComponent |
            ApiV1DeliveryControllersPartialUpdateMetadataErrorComponent |
            ApiV1DeliveryControllersPartialUpdateNameErrorComponent |
            ApiV1DeliveryControllersPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1DeliveryControllersPartialUpdatePlatformServiceErrorComponent |
            ApiV1DeliveryControllersPartialUpdateProviderErrorComponent |
            ApiV1DeliveryControllersPartialUpdateProviderIdErrorComponent |
            ApiV1DeliveryControllersPartialUpdateProviderReferenceErrorComponent |
            ApiV1DeliveryControllersPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1DeliveryControllersPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1DeliveryControllersPartialUpdateSlaTargetErrorComponent |
            ApiV1DeliveryControllersPartialUpdateSloAvailabilityErrorComponent |
            ApiV1DeliveryControllersPartialUpdateSloTargetErrorComponent |
            ApiV1DeliveryControllersPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1DeliveryControllersPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DeliveryControllersPartialUpdateAnnotationsErrorComponent
        | ApiV1DeliveryControllersPartialUpdateApplicationsDegradedErrorComponent
        | ApiV1DeliveryControllersPartialUpdateApplicationsOutOfSyncErrorComponent
        | ApiV1DeliveryControllersPartialUpdateApplicationsSyncedErrorComponent
        | ApiV1DeliveryControllersPartialUpdateApplicationsTotalErrorComponent
        | ApiV1DeliveryControllersPartialUpdateArchivedAtErrorComponent
        | ApiV1DeliveryControllersPartialUpdateArchivedErrorComponent
        | ApiV1DeliveryControllersPartialUpdateArchivedReasonErrorComponent
        | ApiV1DeliveryControllersPartialUpdateControllerAppVersionErrorComponent
        | ApiV1DeliveryControllersPartialUpdateCredentialErrorComponent
        | ApiV1DeliveryControllersPartialUpdateCriticalityErrorComponent
        | ApiV1DeliveryControllersPartialUpdateDebugModeErrorComponent
        | ApiV1DeliveryControllersPartialUpdateDisplayNameErrorComponent
        | ApiV1DeliveryControllersPartialUpdateHostnameErrorComponent
        | ApiV1DeliveryControllersPartialUpdateK8SAppErrorComponent
        | ApiV1DeliveryControllersPartialUpdateK8SClusterErrorComponent
        | ApiV1DeliveryControllersPartialUpdateKindErrorComponent
        | ApiV1DeliveryControllersPartialUpdateLabelsErrorComponent
        | ApiV1DeliveryControllersPartialUpdateMetadataErrorComponent
        | ApiV1DeliveryControllersPartialUpdateNameErrorComponent
        | ApiV1DeliveryControllersPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1DeliveryControllersPartialUpdatePlatformServiceErrorComponent
        | ApiV1DeliveryControllersPartialUpdateProviderErrorComponent
        | ApiV1DeliveryControllersPartialUpdateProviderIdErrorComponent
        | ApiV1DeliveryControllersPartialUpdateProviderReferenceErrorComponent
        | ApiV1DeliveryControllersPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1DeliveryControllersPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1DeliveryControllersPartialUpdateSlaTargetErrorComponent
        | ApiV1DeliveryControllersPartialUpdateSloAvailabilityErrorComponent
        | ApiV1DeliveryControllersPartialUpdateSloTargetErrorComponent
        | ApiV1DeliveryControllersPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1DeliveryControllersPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_delivery_controllers_partial_update_annotations_error_component import (
            ApiV1DeliveryControllersPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_applications_degraded_error_component import (
            ApiV1DeliveryControllersPartialUpdateApplicationsDegradedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_applications_out_of_sync_error_component import (
            ApiV1DeliveryControllersPartialUpdateApplicationsOutOfSyncErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_applications_synced_error_component import (
            ApiV1DeliveryControllersPartialUpdateApplicationsSyncedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_applications_total_error_component import (
            ApiV1DeliveryControllersPartialUpdateApplicationsTotalErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_archived_at_error_component import (
            ApiV1DeliveryControllersPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_archived_error_component import (
            ApiV1DeliveryControllersPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_archived_reason_error_component import (
            ApiV1DeliveryControllersPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_controller_app_version_error_component import (
            ApiV1DeliveryControllersPartialUpdateControllerAppVersionErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_credential_error_component import (
            ApiV1DeliveryControllersPartialUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_criticality_error_component import (
            ApiV1DeliveryControllersPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_debug_mode_error_component import (
            ApiV1DeliveryControllersPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_display_name_error_component import (
            ApiV1DeliveryControllersPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_hostname_error_component import (
            ApiV1DeliveryControllersPartialUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_k8s_app_error_component import (
            ApiV1DeliveryControllersPartialUpdateK8SAppErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_k8s_cluster_error_component import (
            ApiV1DeliveryControllersPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_kind_error_component import (
            ApiV1DeliveryControllersPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_labels_error_component import (
            ApiV1DeliveryControllersPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_name_error_component import (
            ApiV1DeliveryControllersPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_non_field_errors_error_component import (
            ApiV1DeliveryControllersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_platform_service_error_component import (
            ApiV1DeliveryControllersPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_provider_error_component import (
            ApiV1DeliveryControllersPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_provider_id_error_component import (
            ApiV1DeliveryControllersPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_provider_reference_error_component import (
            ApiV1DeliveryControllersPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_reconciliation_enabled_error_component import (
            ApiV1DeliveryControllersPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_sla_availability_error_component import (
            ApiV1DeliveryControllersPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_sla_target_error_component import (
            ApiV1DeliveryControllersPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_slo_availability_error_component import (
            ApiV1DeliveryControllersPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_slo_target_error_component import (
            ApiV1DeliveryControllersPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_target_availability_error_component import (
            ApiV1DeliveryControllersPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_tolerations_error_component import (
            ApiV1DeliveryControllersPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateApplicationsTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateApplicationsSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateApplicationsOutOfSyncErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateApplicationsDegradedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateControllerAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersPartialUpdateCredentialErrorComponent):
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
        from ..models.api_v1_delivery_controllers_partial_update_annotations_error_component import (
            ApiV1DeliveryControllersPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_applications_degraded_error_component import (
            ApiV1DeliveryControllersPartialUpdateApplicationsDegradedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_applications_out_of_sync_error_component import (
            ApiV1DeliveryControllersPartialUpdateApplicationsOutOfSyncErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_applications_synced_error_component import (
            ApiV1DeliveryControllersPartialUpdateApplicationsSyncedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_applications_total_error_component import (
            ApiV1DeliveryControllersPartialUpdateApplicationsTotalErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_archived_at_error_component import (
            ApiV1DeliveryControllersPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_archived_error_component import (
            ApiV1DeliveryControllersPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_archived_reason_error_component import (
            ApiV1DeliveryControllersPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_controller_app_version_error_component import (
            ApiV1DeliveryControllersPartialUpdateControllerAppVersionErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_credential_error_component import (
            ApiV1DeliveryControllersPartialUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_criticality_error_component import (
            ApiV1DeliveryControllersPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_debug_mode_error_component import (
            ApiV1DeliveryControllersPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_display_name_error_component import (
            ApiV1DeliveryControllersPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_hostname_error_component import (
            ApiV1DeliveryControllersPartialUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_k8s_app_error_component import (
            ApiV1DeliveryControllersPartialUpdateK8SAppErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_k8s_cluster_error_component import (
            ApiV1DeliveryControllersPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_kind_error_component import (
            ApiV1DeliveryControllersPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_labels_error_component import (
            ApiV1DeliveryControllersPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_metadata_error_component import (
            ApiV1DeliveryControllersPartialUpdateMetadataErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_name_error_component import (
            ApiV1DeliveryControllersPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_non_field_errors_error_component import (
            ApiV1DeliveryControllersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_platform_service_error_component import (
            ApiV1DeliveryControllersPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_provider_error_component import (
            ApiV1DeliveryControllersPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_provider_id_error_component import (
            ApiV1DeliveryControllersPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_provider_reference_error_component import (
            ApiV1DeliveryControllersPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_reconciliation_enabled_error_component import (
            ApiV1DeliveryControllersPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_sla_availability_error_component import (
            ApiV1DeliveryControllersPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_sla_target_error_component import (
            ApiV1DeliveryControllersPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_slo_availability_error_component import (
            ApiV1DeliveryControllersPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_slo_target_error_component import (
            ApiV1DeliveryControllersPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_target_availability_error_component import (
            ApiV1DeliveryControllersPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_partial_update_tolerations_error_component import (
            ApiV1DeliveryControllersPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DeliveryControllersPartialUpdateAnnotationsErrorComponent
                | ApiV1DeliveryControllersPartialUpdateApplicationsDegradedErrorComponent
                | ApiV1DeliveryControllersPartialUpdateApplicationsOutOfSyncErrorComponent
                | ApiV1DeliveryControllersPartialUpdateApplicationsSyncedErrorComponent
                | ApiV1DeliveryControllersPartialUpdateApplicationsTotalErrorComponent
                | ApiV1DeliveryControllersPartialUpdateArchivedAtErrorComponent
                | ApiV1DeliveryControllersPartialUpdateArchivedErrorComponent
                | ApiV1DeliveryControllersPartialUpdateArchivedReasonErrorComponent
                | ApiV1DeliveryControllersPartialUpdateControllerAppVersionErrorComponent
                | ApiV1DeliveryControllersPartialUpdateCredentialErrorComponent
                | ApiV1DeliveryControllersPartialUpdateCriticalityErrorComponent
                | ApiV1DeliveryControllersPartialUpdateDebugModeErrorComponent
                | ApiV1DeliveryControllersPartialUpdateDisplayNameErrorComponent
                | ApiV1DeliveryControllersPartialUpdateHostnameErrorComponent
                | ApiV1DeliveryControllersPartialUpdateK8SAppErrorComponent
                | ApiV1DeliveryControllersPartialUpdateK8SClusterErrorComponent
                | ApiV1DeliveryControllersPartialUpdateKindErrorComponent
                | ApiV1DeliveryControllersPartialUpdateLabelsErrorComponent
                | ApiV1DeliveryControllersPartialUpdateMetadataErrorComponent
                | ApiV1DeliveryControllersPartialUpdateNameErrorComponent
                | ApiV1DeliveryControllersPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1DeliveryControllersPartialUpdatePlatformServiceErrorComponent
                | ApiV1DeliveryControllersPartialUpdateProviderErrorComponent
                | ApiV1DeliveryControllersPartialUpdateProviderIdErrorComponent
                | ApiV1DeliveryControllersPartialUpdateProviderReferenceErrorComponent
                | ApiV1DeliveryControllersPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1DeliveryControllersPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1DeliveryControllersPartialUpdateSlaTargetErrorComponent
                | ApiV1DeliveryControllersPartialUpdateSloAvailabilityErrorComponent
                | ApiV1DeliveryControllersPartialUpdateSloTargetErrorComponent
                | ApiV1DeliveryControllersPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1DeliveryControllersPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_0 = (
                        ApiV1DeliveryControllersPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_1 = (
                        ApiV1DeliveryControllersPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_2 = (
                        ApiV1DeliveryControllersPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_3 = (
                        ApiV1DeliveryControllersPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_4 = (
                        ApiV1DeliveryControllersPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_5 = (
                        ApiV1DeliveryControllersPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_6 = (
                        ApiV1DeliveryControllersPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_7 = (
                        ApiV1DeliveryControllersPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_8 = (
                        ApiV1DeliveryControllersPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_9 = (
                        ApiV1DeliveryControllersPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_10 = (
                        ApiV1DeliveryControllersPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_11 = (
                        ApiV1DeliveryControllersPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_12 = (
                        ApiV1DeliveryControllersPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_13 = (
                        ApiV1DeliveryControllersPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_14 = (
                        ApiV1DeliveryControllersPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_15 = (
                        ApiV1DeliveryControllersPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_16 = (
                        ApiV1DeliveryControllersPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_17 = (
                        ApiV1DeliveryControllersPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_18 = (
                        ApiV1DeliveryControllersPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_19 = (
                        ApiV1DeliveryControllersPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_20 = (
                        ApiV1DeliveryControllersPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_21 = (
                        ApiV1DeliveryControllersPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_22 = (
                        ApiV1DeliveryControllersPartialUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_23 = (
                        ApiV1DeliveryControllersPartialUpdateApplicationsTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_24 = (
                        ApiV1DeliveryControllersPartialUpdateApplicationsSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_25 = (
                        ApiV1DeliveryControllersPartialUpdateApplicationsOutOfSyncErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_26 = (
                        ApiV1DeliveryControllersPartialUpdateApplicationsDegradedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_27 = (
                        ApiV1DeliveryControllersPartialUpdateControllerAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_28 = (
                        ApiV1DeliveryControllersPartialUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_29 = (
                        ApiV1DeliveryControllersPartialUpdateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_partial_update_error_type_30 = (
                        ApiV1DeliveryControllersPartialUpdateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_delivery_controllers_partial_update_error_type_31 = (
                    ApiV1DeliveryControllersPartialUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_delivery_controllers_partial_update_error_type_31

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_delivery_controllers_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_delivery_controllers_partial_update_validation_error.additional_properties = d
        return api_v1_delivery_controllers_partial_update_validation_error

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
