from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_delivery_controllers_archive_create_annotations_error_component import (
        ApiV1DeliveryControllersArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_applications_degraded_error_component import (
        ApiV1DeliveryControllersArchiveCreateApplicationsDegradedErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_applications_out_of_sync_error_component import (
        ApiV1DeliveryControllersArchiveCreateApplicationsOutOfSyncErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_applications_synced_error_component import (
        ApiV1DeliveryControllersArchiveCreateApplicationsSyncedErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_applications_total_error_component import (
        ApiV1DeliveryControllersArchiveCreateApplicationsTotalErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_archived_at_error_component import (
        ApiV1DeliveryControllersArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_archived_error_component import (
        ApiV1DeliveryControllersArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_archived_reason_error_component import (
        ApiV1DeliveryControllersArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_controller_app_version_error_component import (
        ApiV1DeliveryControllersArchiveCreateControllerAppVersionErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_credential_error_component import (
        ApiV1DeliveryControllersArchiveCreateCredentialErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_criticality_error_component import (
        ApiV1DeliveryControllersArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_debug_mode_error_component import (
        ApiV1DeliveryControllersArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_display_name_error_component import (
        ApiV1DeliveryControllersArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_hostname_error_component import (
        ApiV1DeliveryControllersArchiveCreateHostnameErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_k8s_app_error_component import (
        ApiV1DeliveryControllersArchiveCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_k8s_cluster_error_component import (
        ApiV1DeliveryControllersArchiveCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_kind_error_component import (
        ApiV1DeliveryControllersArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_labels_error_component import (
        ApiV1DeliveryControllersArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_metadata_error_component import (
        ApiV1DeliveryControllersArchiveCreateMetadataErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_name_error_component import (
        ApiV1DeliveryControllersArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_non_field_errors_error_component import (
        ApiV1DeliveryControllersArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_platform_service_error_component import (
        ApiV1DeliveryControllersArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_provider_error_component import (
        ApiV1DeliveryControllersArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_provider_id_error_component import (
        ApiV1DeliveryControllersArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_provider_reference_error_component import (
        ApiV1DeliveryControllersArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_reconciliation_enabled_error_component import (
        ApiV1DeliveryControllersArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_sla_availability_error_component import (
        ApiV1DeliveryControllersArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_sla_target_error_component import (
        ApiV1DeliveryControllersArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_slo_availability_error_component import (
        ApiV1DeliveryControllersArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_slo_target_error_component import (
        ApiV1DeliveryControllersArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_target_availability_error_component import (
        ApiV1DeliveryControllersArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_delivery_controllers_archive_create_tolerations_error_component import (
        ApiV1DeliveryControllersArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DeliveryControllersArchiveCreateValidationError")


@_attrs_define
class ApiV1DeliveryControllersArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DeliveryControllersArchiveCreateAnnotationsErrorComponent |
            ApiV1DeliveryControllersArchiveCreateApplicationsDegradedErrorComponent |
            ApiV1DeliveryControllersArchiveCreateApplicationsOutOfSyncErrorComponent |
            ApiV1DeliveryControllersArchiveCreateApplicationsSyncedErrorComponent |
            ApiV1DeliveryControllersArchiveCreateApplicationsTotalErrorComponent |
            ApiV1DeliveryControllersArchiveCreateArchivedAtErrorComponent |
            ApiV1DeliveryControllersArchiveCreateArchivedErrorComponent |
            ApiV1DeliveryControllersArchiveCreateArchivedReasonErrorComponent |
            ApiV1DeliveryControllersArchiveCreateControllerAppVersionErrorComponent |
            ApiV1DeliveryControllersArchiveCreateCredentialErrorComponent |
            ApiV1DeliveryControllersArchiveCreateCriticalityErrorComponent |
            ApiV1DeliveryControllersArchiveCreateDebugModeErrorComponent |
            ApiV1DeliveryControllersArchiveCreateDisplayNameErrorComponent |
            ApiV1DeliveryControllersArchiveCreateHostnameErrorComponent |
            ApiV1DeliveryControllersArchiveCreateK8SAppErrorComponent |
            ApiV1DeliveryControllersArchiveCreateK8SClusterErrorComponent |
            ApiV1DeliveryControllersArchiveCreateKindErrorComponent |
            ApiV1DeliveryControllersArchiveCreateLabelsErrorComponent |
            ApiV1DeliveryControllersArchiveCreateMetadataErrorComponent |
            ApiV1DeliveryControllersArchiveCreateNameErrorComponent |
            ApiV1DeliveryControllersArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1DeliveryControllersArchiveCreatePlatformServiceErrorComponent |
            ApiV1DeliveryControllersArchiveCreateProviderErrorComponent |
            ApiV1DeliveryControllersArchiveCreateProviderIdErrorComponent |
            ApiV1DeliveryControllersArchiveCreateProviderReferenceErrorComponent |
            ApiV1DeliveryControllersArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1DeliveryControllersArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1DeliveryControllersArchiveCreateSlaTargetErrorComponent |
            ApiV1DeliveryControllersArchiveCreateSloAvailabilityErrorComponent |
            ApiV1DeliveryControllersArchiveCreateSloTargetErrorComponent |
            ApiV1DeliveryControllersArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1DeliveryControllersArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DeliveryControllersArchiveCreateAnnotationsErrorComponent
        | ApiV1DeliveryControllersArchiveCreateApplicationsDegradedErrorComponent
        | ApiV1DeliveryControllersArchiveCreateApplicationsOutOfSyncErrorComponent
        | ApiV1DeliveryControllersArchiveCreateApplicationsSyncedErrorComponent
        | ApiV1DeliveryControllersArchiveCreateApplicationsTotalErrorComponent
        | ApiV1DeliveryControllersArchiveCreateArchivedAtErrorComponent
        | ApiV1DeliveryControllersArchiveCreateArchivedErrorComponent
        | ApiV1DeliveryControllersArchiveCreateArchivedReasonErrorComponent
        | ApiV1DeliveryControllersArchiveCreateControllerAppVersionErrorComponent
        | ApiV1DeliveryControllersArchiveCreateCredentialErrorComponent
        | ApiV1DeliveryControllersArchiveCreateCriticalityErrorComponent
        | ApiV1DeliveryControllersArchiveCreateDebugModeErrorComponent
        | ApiV1DeliveryControllersArchiveCreateDisplayNameErrorComponent
        | ApiV1DeliveryControllersArchiveCreateHostnameErrorComponent
        | ApiV1DeliveryControllersArchiveCreateK8SAppErrorComponent
        | ApiV1DeliveryControllersArchiveCreateK8SClusterErrorComponent
        | ApiV1DeliveryControllersArchiveCreateKindErrorComponent
        | ApiV1DeliveryControllersArchiveCreateLabelsErrorComponent
        | ApiV1DeliveryControllersArchiveCreateMetadataErrorComponent
        | ApiV1DeliveryControllersArchiveCreateNameErrorComponent
        | ApiV1DeliveryControllersArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1DeliveryControllersArchiveCreatePlatformServiceErrorComponent
        | ApiV1DeliveryControllersArchiveCreateProviderErrorComponent
        | ApiV1DeliveryControllersArchiveCreateProviderIdErrorComponent
        | ApiV1DeliveryControllersArchiveCreateProviderReferenceErrorComponent
        | ApiV1DeliveryControllersArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1DeliveryControllersArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1DeliveryControllersArchiveCreateSlaTargetErrorComponent
        | ApiV1DeliveryControllersArchiveCreateSloAvailabilityErrorComponent
        | ApiV1DeliveryControllersArchiveCreateSloTargetErrorComponent
        | ApiV1DeliveryControllersArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1DeliveryControllersArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_delivery_controllers_archive_create_annotations_error_component import (
            ApiV1DeliveryControllersArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_applications_degraded_error_component import (
            ApiV1DeliveryControllersArchiveCreateApplicationsDegradedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_applications_out_of_sync_error_component import (
            ApiV1DeliveryControllersArchiveCreateApplicationsOutOfSyncErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_applications_synced_error_component import (
            ApiV1DeliveryControllersArchiveCreateApplicationsSyncedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_applications_total_error_component import (
            ApiV1DeliveryControllersArchiveCreateApplicationsTotalErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_archived_at_error_component import (
            ApiV1DeliveryControllersArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_archived_error_component import (
            ApiV1DeliveryControllersArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_archived_reason_error_component import (
            ApiV1DeliveryControllersArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_controller_app_version_error_component import (
            ApiV1DeliveryControllersArchiveCreateControllerAppVersionErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_credential_error_component import (
            ApiV1DeliveryControllersArchiveCreateCredentialErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_criticality_error_component import (
            ApiV1DeliveryControllersArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_debug_mode_error_component import (
            ApiV1DeliveryControllersArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_display_name_error_component import (
            ApiV1DeliveryControllersArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_hostname_error_component import (
            ApiV1DeliveryControllersArchiveCreateHostnameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_k8s_app_error_component import (
            ApiV1DeliveryControllersArchiveCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_k8s_cluster_error_component import (
            ApiV1DeliveryControllersArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_kind_error_component import (
            ApiV1DeliveryControllersArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_labels_error_component import (
            ApiV1DeliveryControllersArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_name_error_component import (
            ApiV1DeliveryControllersArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_non_field_errors_error_component import (
            ApiV1DeliveryControllersArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_platform_service_error_component import (
            ApiV1DeliveryControllersArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_provider_error_component import (
            ApiV1DeliveryControllersArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_provider_id_error_component import (
            ApiV1DeliveryControllersArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_provider_reference_error_component import (
            ApiV1DeliveryControllersArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_reconciliation_enabled_error_component import (
            ApiV1DeliveryControllersArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_sla_availability_error_component import (
            ApiV1DeliveryControllersArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_sla_target_error_component import (
            ApiV1DeliveryControllersArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_slo_availability_error_component import (
            ApiV1DeliveryControllersArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_slo_target_error_component import (
            ApiV1DeliveryControllersArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_target_availability_error_component import (
            ApiV1DeliveryControllersArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_tolerations_error_component import (
            ApiV1DeliveryControllersArchiveCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateApplicationsTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateApplicationsSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateApplicationsOutOfSyncErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateApplicationsDegradedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateControllerAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DeliveryControllersArchiveCreateCredentialErrorComponent):
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
        from ..models.api_v1_delivery_controllers_archive_create_annotations_error_component import (
            ApiV1DeliveryControllersArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_applications_degraded_error_component import (
            ApiV1DeliveryControllersArchiveCreateApplicationsDegradedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_applications_out_of_sync_error_component import (
            ApiV1DeliveryControllersArchiveCreateApplicationsOutOfSyncErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_applications_synced_error_component import (
            ApiV1DeliveryControllersArchiveCreateApplicationsSyncedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_applications_total_error_component import (
            ApiV1DeliveryControllersArchiveCreateApplicationsTotalErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_archived_at_error_component import (
            ApiV1DeliveryControllersArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_archived_error_component import (
            ApiV1DeliveryControllersArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_archived_reason_error_component import (
            ApiV1DeliveryControllersArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_controller_app_version_error_component import (
            ApiV1DeliveryControllersArchiveCreateControllerAppVersionErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_credential_error_component import (
            ApiV1DeliveryControllersArchiveCreateCredentialErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_criticality_error_component import (
            ApiV1DeliveryControllersArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_debug_mode_error_component import (
            ApiV1DeliveryControllersArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_display_name_error_component import (
            ApiV1DeliveryControllersArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_hostname_error_component import (
            ApiV1DeliveryControllersArchiveCreateHostnameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_k8s_app_error_component import (
            ApiV1DeliveryControllersArchiveCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_k8s_cluster_error_component import (
            ApiV1DeliveryControllersArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_kind_error_component import (
            ApiV1DeliveryControllersArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_labels_error_component import (
            ApiV1DeliveryControllersArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_metadata_error_component import (
            ApiV1DeliveryControllersArchiveCreateMetadataErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_name_error_component import (
            ApiV1DeliveryControllersArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_non_field_errors_error_component import (
            ApiV1DeliveryControllersArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_platform_service_error_component import (
            ApiV1DeliveryControllersArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_provider_error_component import (
            ApiV1DeliveryControllersArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_provider_id_error_component import (
            ApiV1DeliveryControllersArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_provider_reference_error_component import (
            ApiV1DeliveryControllersArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_reconciliation_enabled_error_component import (
            ApiV1DeliveryControllersArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_sla_availability_error_component import (
            ApiV1DeliveryControllersArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_sla_target_error_component import (
            ApiV1DeliveryControllersArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_slo_availability_error_component import (
            ApiV1DeliveryControllersArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_slo_target_error_component import (
            ApiV1DeliveryControllersArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_target_availability_error_component import (
            ApiV1DeliveryControllersArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_delivery_controllers_archive_create_tolerations_error_component import (
            ApiV1DeliveryControllersArchiveCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DeliveryControllersArchiveCreateAnnotationsErrorComponent
                | ApiV1DeliveryControllersArchiveCreateApplicationsDegradedErrorComponent
                | ApiV1DeliveryControllersArchiveCreateApplicationsOutOfSyncErrorComponent
                | ApiV1DeliveryControllersArchiveCreateApplicationsSyncedErrorComponent
                | ApiV1DeliveryControllersArchiveCreateApplicationsTotalErrorComponent
                | ApiV1DeliveryControllersArchiveCreateArchivedAtErrorComponent
                | ApiV1DeliveryControllersArchiveCreateArchivedErrorComponent
                | ApiV1DeliveryControllersArchiveCreateArchivedReasonErrorComponent
                | ApiV1DeliveryControllersArchiveCreateControllerAppVersionErrorComponent
                | ApiV1DeliveryControllersArchiveCreateCredentialErrorComponent
                | ApiV1DeliveryControllersArchiveCreateCriticalityErrorComponent
                | ApiV1DeliveryControllersArchiveCreateDebugModeErrorComponent
                | ApiV1DeliveryControllersArchiveCreateDisplayNameErrorComponent
                | ApiV1DeliveryControllersArchiveCreateHostnameErrorComponent
                | ApiV1DeliveryControllersArchiveCreateK8SAppErrorComponent
                | ApiV1DeliveryControllersArchiveCreateK8SClusterErrorComponent
                | ApiV1DeliveryControllersArchiveCreateKindErrorComponent
                | ApiV1DeliveryControllersArchiveCreateLabelsErrorComponent
                | ApiV1DeliveryControllersArchiveCreateMetadataErrorComponent
                | ApiV1DeliveryControllersArchiveCreateNameErrorComponent
                | ApiV1DeliveryControllersArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1DeliveryControllersArchiveCreatePlatformServiceErrorComponent
                | ApiV1DeliveryControllersArchiveCreateProviderErrorComponent
                | ApiV1DeliveryControllersArchiveCreateProviderIdErrorComponent
                | ApiV1DeliveryControllersArchiveCreateProviderReferenceErrorComponent
                | ApiV1DeliveryControllersArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1DeliveryControllersArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1DeliveryControllersArchiveCreateSlaTargetErrorComponent
                | ApiV1DeliveryControllersArchiveCreateSloAvailabilityErrorComponent
                | ApiV1DeliveryControllersArchiveCreateSloTargetErrorComponent
                | ApiV1DeliveryControllersArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1DeliveryControllersArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_0 = (
                        ApiV1DeliveryControllersArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_1 = (
                        ApiV1DeliveryControllersArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_2 = (
                        ApiV1DeliveryControllersArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_3 = (
                        ApiV1DeliveryControllersArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_4 = (
                        ApiV1DeliveryControllersArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_5 = (
                        ApiV1DeliveryControllersArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_6 = (
                        ApiV1DeliveryControllersArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_7 = (
                        ApiV1DeliveryControllersArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_8 = (
                        ApiV1DeliveryControllersArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_9 = (
                        ApiV1DeliveryControllersArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_10 = (
                        ApiV1DeliveryControllersArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_11 = (
                        ApiV1DeliveryControllersArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_12 = (
                        ApiV1DeliveryControllersArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_13 = (
                        ApiV1DeliveryControllersArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_14 = (
                        ApiV1DeliveryControllersArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_15 = (
                        ApiV1DeliveryControllersArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_16 = (
                        ApiV1DeliveryControllersArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_17 = (
                        ApiV1DeliveryControllersArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_18 = (
                        ApiV1DeliveryControllersArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_19 = (
                        ApiV1DeliveryControllersArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_20 = (
                        ApiV1DeliveryControllersArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_21 = (
                        ApiV1DeliveryControllersArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_22 = (
                        ApiV1DeliveryControllersArchiveCreateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_23 = (
                        ApiV1DeliveryControllersArchiveCreateApplicationsTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_24 = (
                        ApiV1DeliveryControllersArchiveCreateApplicationsSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_25 = (
                        ApiV1DeliveryControllersArchiveCreateApplicationsOutOfSyncErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_26 = (
                        ApiV1DeliveryControllersArchiveCreateApplicationsDegradedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_27 = (
                        ApiV1DeliveryControllersArchiveCreateControllerAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_28 = (
                        ApiV1DeliveryControllersArchiveCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_29 = (
                        ApiV1DeliveryControllersArchiveCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_delivery_controllers_archive_create_error_type_30 = (
                        ApiV1DeliveryControllersArchiveCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_delivery_controllers_archive_create_error_type_31 = (
                    ApiV1DeliveryControllersArchiveCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_delivery_controllers_archive_create_error_type_31

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_delivery_controllers_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_delivery_controllers_archive_create_validation_error.additional_properties = d
        return api_v1_delivery_controllers_archive_create_validation_error

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
