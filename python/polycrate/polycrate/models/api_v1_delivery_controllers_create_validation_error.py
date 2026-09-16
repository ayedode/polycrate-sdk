from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_delivery_controllers_create_annotations_error_component import (
        ApiV1DeliveryControllersCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_applications_degraded_error_component import (
        ApiV1DeliveryControllersCreateApplicationsDegradedErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_applications_out_of_sync_error_component import (
        ApiV1DeliveryControllersCreateApplicationsOutOfSyncErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_applications_synced_error_component import (
        ApiV1DeliveryControllersCreateApplicationsSyncedErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_applications_total_error_component import (
        ApiV1DeliveryControllersCreateApplicationsTotalErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_archived_at_error_component import (
        ApiV1DeliveryControllersCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_archived_error_component import (
        ApiV1DeliveryControllersCreateArchivedErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_archived_reason_error_component import (
        ApiV1DeliveryControllersCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_controller_app_version_error_component import (
        ApiV1DeliveryControllersCreateControllerAppVersionErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_credential_error_component import (
        ApiV1DeliveryControllersCreateCredentialErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_criticality_error_component import (
        ApiV1DeliveryControllersCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_debug_mode_error_component import (
        ApiV1DeliveryControllersCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_display_name_error_component import (
        ApiV1DeliveryControllersCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_hostname_error_component import (
        ApiV1DeliveryControllersCreateHostnameErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_k8s_app_error_component import (
        ApiV1DeliveryControllersCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_k8s_cluster_error_component import (
        ApiV1DeliveryControllersCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_kind_error_component import (
        ApiV1DeliveryControllersCreateKindErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_labels_error_component import (
        ApiV1DeliveryControllersCreateLabelsErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_metadata_error_component import (
        ApiV1DeliveryControllersCreateMetadataErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_name_error_component import (
        ApiV1DeliveryControllersCreateNameErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_non_field_errors_error_component import (
        ApiV1DeliveryControllersCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_platform_service_error_component import (
        ApiV1DeliveryControllersCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_provider_error_component import (
        ApiV1DeliveryControllersCreateProviderErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_provider_id_error_component import (
        ApiV1DeliveryControllersCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_provider_reference_error_component import (
        ApiV1DeliveryControllersCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_reconciliation_enabled_error_component import (
        ApiV1DeliveryControllersCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_sla_availability_error_component import (
        ApiV1DeliveryControllersCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_sla_target_error_component import (
        ApiV1DeliveryControllersCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_slo_availability_error_component import (
        ApiV1DeliveryControllersCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_slo_target_error_component import (
        ApiV1DeliveryControllersCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_target_availability_error_component import (
        ApiV1DeliveryControllersCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_create_tolerations_error_component import (
        ApiV1DeliveryControllersCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DeliveryControllersCreateValidationError")


@_attrs_define
class ApiV1DeliveryControllersCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DeliveryControllersCreateAnnotationsErrorComponent |
            ApiV1DeliveryControllersCreateApplicationsDegradedErrorComponent |
            ApiV1DeliveryControllersCreateApplicationsOutOfSyncErrorComponent |
            ApiV1DeliveryControllersCreateApplicationsSyncedErrorComponent |
            ApiV1DeliveryControllersCreateApplicationsTotalErrorComponent |
            ApiV1DeliveryControllersCreateArchivedAtErrorComponent | ApiV1DeliveryControllersCreateArchivedErrorComponent |
            ApiV1DeliveryControllersCreateArchivedReasonErrorComponent |
            ApiV1DeliveryControllersCreateControllerAppVersionErrorComponent |
            ApiV1DeliveryControllersCreateCredentialErrorComponent | ApiV1DeliveryControllersCreateCriticalityErrorComponent
            | ApiV1DeliveryControllersCreateDebugModeErrorComponent |
            ApiV1DeliveryControllersCreateDisplayNameErrorComponent | ApiV1DeliveryControllersCreateHostnameErrorComponent |
            ApiV1DeliveryControllersCreateK8SAppErrorComponent | ApiV1DeliveryControllersCreateK8SClusterErrorComponent |
            ApiV1DeliveryControllersCreateKindErrorComponent | ApiV1DeliveryControllersCreateLabelsErrorComponent |
            ApiV1DeliveryControllersCreateMetadataErrorComponent | ApiV1DeliveryControllersCreateNameErrorComponent |
            ApiV1DeliveryControllersCreateNonFieldErrorsErrorComponent |
            ApiV1DeliveryControllersCreatePlatformServiceErrorComponent |
            ApiV1DeliveryControllersCreateProviderErrorComponent | ApiV1DeliveryControllersCreateProviderIdErrorComponent |
            ApiV1DeliveryControllersCreateProviderReferenceErrorComponent |
            ApiV1DeliveryControllersCreateReconciliationEnabledErrorComponent |
            ApiV1DeliveryControllersCreateSlaAvailabilityErrorComponent |
            ApiV1DeliveryControllersCreateSlaTargetErrorComponent |
            ApiV1DeliveryControllersCreateSloAvailabilityErrorComponent |
            ApiV1DeliveryControllersCreateSloTargetErrorComponent |
            ApiV1DeliveryControllersCreateTargetAvailabilityErrorComponent |
            ApiV1DeliveryControllersCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DeliveryControllersCreateAnnotationsErrorComponent
        | ApiV1DeliveryControllersCreateApplicationsDegradedErrorComponent
        | ApiV1DeliveryControllersCreateApplicationsOutOfSyncErrorComponent
        | ApiV1DeliveryControllersCreateApplicationsSyncedErrorComponent
        | ApiV1DeliveryControllersCreateApplicationsTotalErrorComponent
        | ApiV1DeliveryControllersCreateArchivedAtErrorComponent
        | ApiV1DeliveryControllersCreateArchivedErrorComponent
        | ApiV1DeliveryControllersCreateArchivedReasonErrorComponent
        | ApiV1DeliveryControllersCreateControllerAppVersionErrorComponent
        | ApiV1DeliveryControllersCreateCredentialErrorComponent
        | ApiV1DeliveryControllersCreateCriticalityErrorComponent
        | ApiV1DeliveryControllersCreateDebugModeErrorComponent
        | ApiV1DeliveryControllersCreateDisplayNameErrorComponent
        | ApiV1DeliveryControllersCreateHostnameErrorComponent
        | ApiV1DeliveryControllersCreateK8SAppErrorComponent
        | ApiV1DeliveryControllersCreateK8SClusterErrorComponent
        | ApiV1DeliveryControllersCreateKindErrorComponent
        | ApiV1DeliveryControllersCreateLabelsErrorComponent
        | ApiV1DeliveryControllersCreateMetadataErrorComponent
        | ApiV1DeliveryControllersCreateNameErrorComponent
        | ApiV1DeliveryControllersCreateNonFieldErrorsErrorComponent
        | ApiV1DeliveryControllersCreatePlatformServiceErrorComponent
        | ApiV1DeliveryControllersCreateProviderErrorComponent
        | ApiV1DeliveryControllersCreateProviderIdErrorComponent
        | ApiV1DeliveryControllersCreateProviderReferenceErrorComponent
        | ApiV1DeliveryControllersCreateReconciliationEnabledErrorComponent
        | ApiV1DeliveryControllersCreateSlaAvailabilityErrorComponent
        | ApiV1DeliveryControllersCreateSlaTargetErrorComponent
        | ApiV1DeliveryControllersCreateSloAvailabilityErrorComponent
        | ApiV1DeliveryControllersCreateSloTargetErrorComponent
        | ApiV1DeliveryControllersCreateTargetAvailabilityErrorComponent
        | ApiV1DeliveryControllersCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_delivery_controllers_create_annotations_error_component import (
            ApiV1DeliveryControllersCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_applications_degraded_error_component import (
            ApiV1DeliveryControllersCreateApplicationsDegradedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_applications_out_of_sync_error_component import (
            ApiV1DeliveryControllersCreateApplicationsOutOfSyncErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_applications_synced_error_component import (
            ApiV1DeliveryControllersCreateApplicationsSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_applications_total_error_component import (
            ApiV1DeliveryControllersCreateApplicationsTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_archived_at_error_component import (
            ApiV1DeliveryControllersCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_archived_error_component import (
            ApiV1DeliveryControllersCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_archived_reason_error_component import (
            ApiV1DeliveryControllersCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_controller_app_version_error_component import (
            ApiV1DeliveryControllersCreateControllerAppVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_credential_error_component import (
            ApiV1DeliveryControllersCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_criticality_error_component import (
            ApiV1DeliveryControllersCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_debug_mode_error_component import (
            ApiV1DeliveryControllersCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_display_name_error_component import (
            ApiV1DeliveryControllersCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_hostname_error_component import (
            ApiV1DeliveryControllersCreateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_k8s_app_error_component import (
            ApiV1DeliveryControllersCreateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_k8s_cluster_error_component import (
            ApiV1DeliveryControllersCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_kind_error_component import (
            ApiV1DeliveryControllersCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_labels_error_component import (
            ApiV1DeliveryControllersCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_name_error_component import (
            ApiV1DeliveryControllersCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_non_field_errors_error_component import (
            ApiV1DeliveryControllersCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_platform_service_error_component import (
            ApiV1DeliveryControllersCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_provider_error_component import (
            ApiV1DeliveryControllersCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_provider_id_error_component import (
            ApiV1DeliveryControllersCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_provider_reference_error_component import (
            ApiV1DeliveryControllersCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_reconciliation_enabled_error_component import (
            ApiV1DeliveryControllersCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_sla_availability_error_component import (
            ApiV1DeliveryControllersCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_sla_target_error_component import (
            ApiV1DeliveryControllersCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_slo_availability_error_component import (
            ApiV1DeliveryControllersCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_slo_target_error_component import (
            ApiV1DeliveryControllersCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_target_availability_error_component import (
            ApiV1DeliveryControllersCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_tolerations_error_component import (
            ApiV1DeliveryControllersCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DeliveryControllersCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateApplicationsTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateApplicationsSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateApplicationsOutOfSyncErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateApplicationsDegradedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateControllerAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersCreateCredentialErrorComponent):
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
        from ..models.api_v1_delivery_controllers_create_annotations_error_component import (
            ApiV1DeliveryControllersCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_applications_degraded_error_component import (
            ApiV1DeliveryControllersCreateApplicationsDegradedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_applications_out_of_sync_error_component import (
            ApiV1DeliveryControllersCreateApplicationsOutOfSyncErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_applications_synced_error_component import (
            ApiV1DeliveryControllersCreateApplicationsSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_applications_total_error_component import (
            ApiV1DeliveryControllersCreateApplicationsTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_archived_at_error_component import (
            ApiV1DeliveryControllersCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_archived_error_component import (
            ApiV1DeliveryControllersCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_archived_reason_error_component import (
            ApiV1DeliveryControllersCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_controller_app_version_error_component import (
            ApiV1DeliveryControllersCreateControllerAppVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_credential_error_component import (
            ApiV1DeliveryControllersCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_criticality_error_component import (
            ApiV1DeliveryControllersCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_debug_mode_error_component import (
            ApiV1DeliveryControllersCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_display_name_error_component import (
            ApiV1DeliveryControllersCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_hostname_error_component import (
            ApiV1DeliveryControllersCreateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_k8s_app_error_component import (
            ApiV1DeliveryControllersCreateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_k8s_cluster_error_component import (
            ApiV1DeliveryControllersCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_kind_error_component import (
            ApiV1DeliveryControllersCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_labels_error_component import (
            ApiV1DeliveryControllersCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_metadata_error_component import (
            ApiV1DeliveryControllersCreateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_name_error_component import (
            ApiV1DeliveryControllersCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_non_field_errors_error_component import (
            ApiV1DeliveryControllersCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_platform_service_error_component import (
            ApiV1DeliveryControllersCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_provider_error_component import (
            ApiV1DeliveryControllersCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_provider_id_error_component import (
            ApiV1DeliveryControllersCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_provider_reference_error_component import (
            ApiV1DeliveryControllersCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_reconciliation_enabled_error_component import (
            ApiV1DeliveryControllersCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_sla_availability_error_component import (
            ApiV1DeliveryControllersCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_sla_target_error_component import (
            ApiV1DeliveryControllersCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_slo_availability_error_component import (
            ApiV1DeliveryControllersCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_slo_target_error_component import (
            ApiV1DeliveryControllersCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_target_availability_error_component import (
            ApiV1DeliveryControllersCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_delivery_controllers_create_tolerations_error_component import (
            ApiV1DeliveryControllersCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DeliveryControllersCreateAnnotationsErrorComponent
                | ApiV1DeliveryControllersCreateApplicationsDegradedErrorComponent
                | ApiV1DeliveryControllersCreateApplicationsOutOfSyncErrorComponent
                | ApiV1DeliveryControllersCreateApplicationsSyncedErrorComponent
                | ApiV1DeliveryControllersCreateApplicationsTotalErrorComponent
                | ApiV1DeliveryControllersCreateArchivedAtErrorComponent
                | ApiV1DeliveryControllersCreateArchivedErrorComponent
                | ApiV1DeliveryControllersCreateArchivedReasonErrorComponent
                | ApiV1DeliveryControllersCreateControllerAppVersionErrorComponent
                | ApiV1DeliveryControllersCreateCredentialErrorComponent
                | ApiV1DeliveryControllersCreateCriticalityErrorComponent
                | ApiV1DeliveryControllersCreateDebugModeErrorComponent
                | ApiV1DeliveryControllersCreateDisplayNameErrorComponent
                | ApiV1DeliveryControllersCreateHostnameErrorComponent
                | ApiV1DeliveryControllersCreateK8SAppErrorComponent
                | ApiV1DeliveryControllersCreateK8SClusterErrorComponent
                | ApiV1DeliveryControllersCreateKindErrorComponent
                | ApiV1DeliveryControllersCreateLabelsErrorComponent
                | ApiV1DeliveryControllersCreateMetadataErrorComponent
                | ApiV1DeliveryControllersCreateNameErrorComponent
                | ApiV1DeliveryControllersCreateNonFieldErrorsErrorComponent
                | ApiV1DeliveryControllersCreatePlatformServiceErrorComponent
                | ApiV1DeliveryControllersCreateProviderErrorComponent
                | ApiV1DeliveryControllersCreateProviderIdErrorComponent
                | ApiV1DeliveryControllersCreateProviderReferenceErrorComponent
                | ApiV1DeliveryControllersCreateReconciliationEnabledErrorComponent
                | ApiV1DeliveryControllersCreateSlaAvailabilityErrorComponent
                | ApiV1DeliveryControllersCreateSlaTargetErrorComponent
                | ApiV1DeliveryControllersCreateSloAvailabilityErrorComponent
                | ApiV1DeliveryControllersCreateSloTargetErrorComponent
                | ApiV1DeliveryControllersCreateTargetAvailabilityErrorComponent
                | ApiV1DeliveryControllersCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_0 = (
                        ApiV1DeliveryControllersCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_1 = (
                        ApiV1DeliveryControllersCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_2 = (
                        ApiV1DeliveryControllersCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_3 = (
                        ApiV1DeliveryControllersCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_4 = (
                        ApiV1DeliveryControllersCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_5 = (
                        ApiV1DeliveryControllersCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_6 = (
                        ApiV1DeliveryControllersCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_7 = (
                        ApiV1DeliveryControllersCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_8 = (
                        ApiV1DeliveryControllersCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_9 = (
                        ApiV1DeliveryControllersCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_10 = (
                        ApiV1DeliveryControllersCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_11 = (
                        ApiV1DeliveryControllersCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_12 = (
                        ApiV1DeliveryControllersCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_13 = (
                        ApiV1DeliveryControllersCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_14 = (
                        ApiV1DeliveryControllersCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_15 = (
                        ApiV1DeliveryControllersCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_16 = (
                        ApiV1DeliveryControllersCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_17 = (
                        ApiV1DeliveryControllersCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_18 = (
                        ApiV1DeliveryControllersCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_19 = (
                        ApiV1DeliveryControllersCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_20 = (
                        ApiV1DeliveryControllersCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_21 = (
                        ApiV1DeliveryControllersCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_22 = (
                        ApiV1DeliveryControllersCreateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_23 = (
                        ApiV1DeliveryControllersCreateApplicationsTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_24 = (
                        ApiV1DeliveryControllersCreateApplicationsSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_25 = (
                        ApiV1DeliveryControllersCreateApplicationsOutOfSyncErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_26 = (
                        ApiV1DeliveryControllersCreateApplicationsDegradedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_27 = (
                        ApiV1DeliveryControllersCreateControllerAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_28 = (
                        ApiV1DeliveryControllersCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_29 = (
                        ApiV1DeliveryControllersCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_create_error_type_30 = (
                        ApiV1DeliveryControllersCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_delivery_controllers_create_error_type_31 = (
                    ApiV1DeliveryControllersCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_delivery_controllers_create_error_type_31

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_delivery_controllers_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_delivery_controllers_create_validation_error.additional_properties = d
        return api_v1_delivery_controllers_create_validation_error

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
