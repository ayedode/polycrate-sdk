from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_artifact_packages_create_annotations_error_component import (
        ApiV1ArtifactPackagesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_archived_at_error_component import (
        ApiV1ArtifactPackagesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_archived_by_error_component import (
        ApiV1ArtifactPackagesCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_archived_error_component import (
        ApiV1ArtifactPackagesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_archived_reason_error_component import (
        ApiV1ArtifactPackagesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_created_by_component_error_component import (
        ApiV1ArtifactPackagesCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_created_by_user_error_component import (
        ApiV1ArtifactPackagesCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_criticality_error_component import (
        ApiV1ArtifactPackagesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_debug_mode_error_component import (
        ApiV1ArtifactPackagesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_display_name_error_component import (
        ApiV1ArtifactPackagesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_kind_error_component import (
        ApiV1ArtifactPackagesCreateKindErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_labels_error_component import (
        ApiV1ArtifactPackagesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1ArtifactPackagesCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_managed_by_content_type_error_component import (
        ApiV1ArtifactPackagesCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_managed_by_object_id_error_component import (
        ApiV1ArtifactPackagesCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_modified_by_user_error_component import (
        ApiV1ArtifactPackagesCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_name_error_component import (
        ApiV1ArtifactPackagesCreateNameErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_non_field_errors_error_component import (
        ApiV1ArtifactPackagesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_platform_dns_record_created_error_component import (
        ApiV1ArtifactPackagesCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_platform_service_error_component import (
        ApiV1ArtifactPackagesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_provider_error_component import (
        ApiV1ArtifactPackagesCreateProviderErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_provider_id_error_component import (
        ApiV1ArtifactPackagesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_provider_reference_error_component import (
        ApiV1ArtifactPackagesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_raw_data_error_component import (
        ApiV1ArtifactPackagesCreateRawDataErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_reconciliation_enabled_error_component import (
        ApiV1ArtifactPackagesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_sla_availability_error_component import (
        ApiV1ArtifactPackagesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_sla_target_error_component import (
        ApiV1ArtifactPackagesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_sla_window_days_error_component import (
        ApiV1ArtifactPackagesCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_slo_availability_error_component import (
        ApiV1ArtifactPackagesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_slo_target_error_component import (
        ApiV1ArtifactPackagesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_slo_window_days_error_component import (
        ApiV1ArtifactPackagesCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_target_availability_error_component import (
        ApiV1ArtifactPackagesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_create_tolerations_error_component import (
        ApiV1ArtifactPackagesCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ArtifactPackagesCreateValidationError")


@_attrs_define
class ApiV1ArtifactPackagesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ArtifactPackagesCreateAnnotationsErrorComponent |
            ApiV1ArtifactPackagesCreateArchivedAtErrorComponent | ApiV1ArtifactPackagesCreateArchivedByErrorComponent |
            ApiV1ArtifactPackagesCreateArchivedErrorComponent | ApiV1ArtifactPackagesCreateArchivedReasonErrorComponent |
            ApiV1ArtifactPackagesCreateCreatedByComponentErrorComponent |
            ApiV1ArtifactPackagesCreateCreatedByUserErrorComponent | ApiV1ArtifactPackagesCreateCriticalityErrorComponent |
            ApiV1ArtifactPackagesCreateDebugModeErrorComponent | ApiV1ArtifactPackagesCreateDisplayNameErrorComponent |
            ApiV1ArtifactPackagesCreateKindErrorComponent | ApiV1ArtifactPackagesCreateLabelsErrorComponent |
            ApiV1ArtifactPackagesCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1ArtifactPackagesCreateManagedByContentTypeErrorComponent |
            ApiV1ArtifactPackagesCreateManagedByObjectIdErrorComponent |
            ApiV1ArtifactPackagesCreateModifiedByUserErrorComponent | ApiV1ArtifactPackagesCreateNameErrorComponent |
            ApiV1ArtifactPackagesCreateNonFieldErrorsErrorComponent |
            ApiV1ArtifactPackagesCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ArtifactPackagesCreatePlatformServiceErrorComponent | ApiV1ArtifactPackagesCreateProviderErrorComponent |
            ApiV1ArtifactPackagesCreateProviderIdErrorComponent | ApiV1ArtifactPackagesCreateProviderReferenceErrorComponent
            | ApiV1ArtifactPackagesCreateRawDataErrorComponent |
            ApiV1ArtifactPackagesCreateReconciliationEnabledErrorComponent |
            ApiV1ArtifactPackagesCreateSlaAvailabilityErrorComponent | ApiV1ArtifactPackagesCreateSlaTargetErrorComponent |
            ApiV1ArtifactPackagesCreateSlaWindowDaysErrorComponent |
            ApiV1ArtifactPackagesCreateSloAvailabilityErrorComponent | ApiV1ArtifactPackagesCreateSloTargetErrorComponent |
            ApiV1ArtifactPackagesCreateSloWindowDaysErrorComponent |
            ApiV1ArtifactPackagesCreateTargetAvailabilityErrorComponent |
            ApiV1ArtifactPackagesCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ArtifactPackagesCreateAnnotationsErrorComponent
        | ApiV1ArtifactPackagesCreateArchivedAtErrorComponent
        | ApiV1ArtifactPackagesCreateArchivedByErrorComponent
        | ApiV1ArtifactPackagesCreateArchivedErrorComponent
        | ApiV1ArtifactPackagesCreateArchivedReasonErrorComponent
        | ApiV1ArtifactPackagesCreateCreatedByComponentErrorComponent
        | ApiV1ArtifactPackagesCreateCreatedByUserErrorComponent
        | ApiV1ArtifactPackagesCreateCriticalityErrorComponent
        | ApiV1ArtifactPackagesCreateDebugModeErrorComponent
        | ApiV1ArtifactPackagesCreateDisplayNameErrorComponent
        | ApiV1ArtifactPackagesCreateKindErrorComponent
        | ApiV1ArtifactPackagesCreateLabelsErrorComponent
        | ApiV1ArtifactPackagesCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ArtifactPackagesCreateManagedByContentTypeErrorComponent
        | ApiV1ArtifactPackagesCreateManagedByObjectIdErrorComponent
        | ApiV1ArtifactPackagesCreateModifiedByUserErrorComponent
        | ApiV1ArtifactPackagesCreateNameErrorComponent
        | ApiV1ArtifactPackagesCreateNonFieldErrorsErrorComponent
        | ApiV1ArtifactPackagesCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ArtifactPackagesCreatePlatformServiceErrorComponent
        | ApiV1ArtifactPackagesCreateProviderErrorComponent
        | ApiV1ArtifactPackagesCreateProviderIdErrorComponent
        | ApiV1ArtifactPackagesCreateProviderReferenceErrorComponent
        | ApiV1ArtifactPackagesCreateRawDataErrorComponent
        | ApiV1ArtifactPackagesCreateReconciliationEnabledErrorComponent
        | ApiV1ArtifactPackagesCreateSlaAvailabilityErrorComponent
        | ApiV1ArtifactPackagesCreateSlaTargetErrorComponent
        | ApiV1ArtifactPackagesCreateSlaWindowDaysErrorComponent
        | ApiV1ArtifactPackagesCreateSloAvailabilityErrorComponent
        | ApiV1ArtifactPackagesCreateSloTargetErrorComponent
        | ApiV1ArtifactPackagesCreateSloWindowDaysErrorComponent
        | ApiV1ArtifactPackagesCreateTargetAvailabilityErrorComponent
        | ApiV1ArtifactPackagesCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_artifact_packages_create_annotations_error_component import (
            ApiV1ArtifactPackagesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_archived_at_error_component import (
            ApiV1ArtifactPackagesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_archived_by_error_component import (
            ApiV1ArtifactPackagesCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_archived_error_component import (
            ApiV1ArtifactPackagesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_archived_reason_error_component import (
            ApiV1ArtifactPackagesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_created_by_component_error_component import (
            ApiV1ArtifactPackagesCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_criticality_error_component import (
            ApiV1ArtifactPackagesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_debug_mode_error_component import (
            ApiV1ArtifactPackagesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_display_name_error_component import (
            ApiV1ArtifactPackagesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_kind_error_component import (
            ApiV1ArtifactPackagesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_labels_error_component import (
            ApiV1ArtifactPackagesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactPackagesCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_managed_by_content_type_error_component import (
            ApiV1ArtifactPackagesCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_managed_by_object_id_error_component import (
            ApiV1ArtifactPackagesCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_modified_by_user_error_component import (
            ApiV1ArtifactPackagesCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_name_error_component import (
            ApiV1ArtifactPackagesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_non_field_errors_error_component import (
            ApiV1ArtifactPackagesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_platform_dns_record_created_error_component import (
            ApiV1ArtifactPackagesCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_platform_service_error_component import (
            ApiV1ArtifactPackagesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_provider_error_component import (
            ApiV1ArtifactPackagesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_provider_id_error_component import (
            ApiV1ArtifactPackagesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_provider_reference_error_component import (
            ApiV1ArtifactPackagesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_raw_data_error_component import (
            ApiV1ArtifactPackagesCreateRawDataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_reconciliation_enabled_error_component import (
            ApiV1ArtifactPackagesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_sla_availability_error_component import (
            ApiV1ArtifactPackagesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_sla_target_error_component import (
            ApiV1ArtifactPackagesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_sla_window_days_error_component import (
            ApiV1ArtifactPackagesCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_slo_availability_error_component import (
            ApiV1ArtifactPackagesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_slo_target_error_component import (
            ApiV1ArtifactPackagesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_slo_window_days_error_component import (
            ApiV1ArtifactPackagesCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_target_availability_error_component import (
            ApiV1ArtifactPackagesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_tolerations_error_component import (
            ApiV1ArtifactPackagesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ArtifactPackagesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactPackagesCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateRawDataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesCreateModifiedByUserErrorComponent):
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
        from ..models.api_v1_artifact_packages_create_annotations_error_component import (
            ApiV1ArtifactPackagesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_archived_at_error_component import (
            ApiV1ArtifactPackagesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_archived_by_error_component import (
            ApiV1ArtifactPackagesCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_archived_error_component import (
            ApiV1ArtifactPackagesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_archived_reason_error_component import (
            ApiV1ArtifactPackagesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_created_by_component_error_component import (
            ApiV1ArtifactPackagesCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_created_by_user_error_component import (
            ApiV1ArtifactPackagesCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_criticality_error_component import (
            ApiV1ArtifactPackagesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_debug_mode_error_component import (
            ApiV1ArtifactPackagesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_display_name_error_component import (
            ApiV1ArtifactPackagesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_kind_error_component import (
            ApiV1ArtifactPackagesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_labels_error_component import (
            ApiV1ArtifactPackagesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactPackagesCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_managed_by_content_type_error_component import (
            ApiV1ArtifactPackagesCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_managed_by_object_id_error_component import (
            ApiV1ArtifactPackagesCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_modified_by_user_error_component import (
            ApiV1ArtifactPackagesCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_name_error_component import (
            ApiV1ArtifactPackagesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_non_field_errors_error_component import (
            ApiV1ArtifactPackagesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_platform_dns_record_created_error_component import (
            ApiV1ArtifactPackagesCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_platform_service_error_component import (
            ApiV1ArtifactPackagesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_provider_error_component import (
            ApiV1ArtifactPackagesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_provider_id_error_component import (
            ApiV1ArtifactPackagesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_provider_reference_error_component import (
            ApiV1ArtifactPackagesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_raw_data_error_component import (
            ApiV1ArtifactPackagesCreateRawDataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_reconciliation_enabled_error_component import (
            ApiV1ArtifactPackagesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_sla_availability_error_component import (
            ApiV1ArtifactPackagesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_sla_target_error_component import (
            ApiV1ArtifactPackagesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_sla_window_days_error_component import (
            ApiV1ArtifactPackagesCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_slo_availability_error_component import (
            ApiV1ArtifactPackagesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_slo_target_error_component import (
            ApiV1ArtifactPackagesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_slo_window_days_error_component import (
            ApiV1ArtifactPackagesCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_target_availability_error_component import (
            ApiV1ArtifactPackagesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_create_tolerations_error_component import (
            ApiV1ArtifactPackagesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ArtifactPackagesCreateAnnotationsErrorComponent
                | ApiV1ArtifactPackagesCreateArchivedAtErrorComponent
                | ApiV1ArtifactPackagesCreateArchivedByErrorComponent
                | ApiV1ArtifactPackagesCreateArchivedErrorComponent
                | ApiV1ArtifactPackagesCreateArchivedReasonErrorComponent
                | ApiV1ArtifactPackagesCreateCreatedByComponentErrorComponent
                | ApiV1ArtifactPackagesCreateCreatedByUserErrorComponent
                | ApiV1ArtifactPackagesCreateCriticalityErrorComponent
                | ApiV1ArtifactPackagesCreateDebugModeErrorComponent
                | ApiV1ArtifactPackagesCreateDisplayNameErrorComponent
                | ApiV1ArtifactPackagesCreateKindErrorComponent
                | ApiV1ArtifactPackagesCreateLabelsErrorComponent
                | ApiV1ArtifactPackagesCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ArtifactPackagesCreateManagedByContentTypeErrorComponent
                | ApiV1ArtifactPackagesCreateManagedByObjectIdErrorComponent
                | ApiV1ArtifactPackagesCreateModifiedByUserErrorComponent
                | ApiV1ArtifactPackagesCreateNameErrorComponent
                | ApiV1ArtifactPackagesCreateNonFieldErrorsErrorComponent
                | ApiV1ArtifactPackagesCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ArtifactPackagesCreatePlatformServiceErrorComponent
                | ApiV1ArtifactPackagesCreateProviderErrorComponent
                | ApiV1ArtifactPackagesCreateProviderIdErrorComponent
                | ApiV1ArtifactPackagesCreateProviderReferenceErrorComponent
                | ApiV1ArtifactPackagesCreateRawDataErrorComponent
                | ApiV1ArtifactPackagesCreateReconciliationEnabledErrorComponent
                | ApiV1ArtifactPackagesCreateSlaAvailabilityErrorComponent
                | ApiV1ArtifactPackagesCreateSlaTargetErrorComponent
                | ApiV1ArtifactPackagesCreateSlaWindowDaysErrorComponent
                | ApiV1ArtifactPackagesCreateSloAvailabilityErrorComponent
                | ApiV1ArtifactPackagesCreateSloTargetErrorComponent
                | ApiV1ArtifactPackagesCreateSloWindowDaysErrorComponent
                | ApiV1ArtifactPackagesCreateTargetAvailabilityErrorComponent
                | ApiV1ArtifactPackagesCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_0 = (
                        ApiV1ArtifactPackagesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_1 = (
                        ApiV1ArtifactPackagesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_2 = (
                        ApiV1ArtifactPackagesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_3 = (
                        ApiV1ArtifactPackagesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_4 = (
                        ApiV1ArtifactPackagesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_5 = (
                        ApiV1ArtifactPackagesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_6 = (
                        ApiV1ArtifactPackagesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_7 = (
                        ApiV1ArtifactPackagesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_8 = (
                        ApiV1ArtifactPackagesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_9 = (
                        ApiV1ArtifactPackagesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_10 = (
                        ApiV1ArtifactPackagesCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_11 = (
                        ApiV1ArtifactPackagesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_12 = (
                        ApiV1ArtifactPackagesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_13 = (
                        ApiV1ArtifactPackagesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_14 = (
                        ApiV1ArtifactPackagesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_15 = (
                        ApiV1ArtifactPackagesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_16 = (
                        ApiV1ArtifactPackagesCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_17 = (
                        ApiV1ArtifactPackagesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_18 = (
                        ApiV1ArtifactPackagesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_19 = (
                        ApiV1ArtifactPackagesCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_20 = (
                        ApiV1ArtifactPackagesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_21 = (
                        ApiV1ArtifactPackagesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_22 = (
                        ApiV1ArtifactPackagesCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_23 = (
                        ApiV1ArtifactPackagesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_24 = (
                        ApiV1ArtifactPackagesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_25 = (
                        ApiV1ArtifactPackagesCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_26 = (
                        ApiV1ArtifactPackagesCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_27 = (
                        ApiV1ArtifactPackagesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_28 = (
                        ApiV1ArtifactPackagesCreateRawDataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_29 = (
                        ApiV1ArtifactPackagesCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_30 = (
                        ApiV1ArtifactPackagesCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_create_error_type_31 = (
                        ApiV1ArtifactPackagesCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_artifact_packages_create_error_type_32 = (
                    ApiV1ArtifactPackagesCreateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_artifact_packages_create_error_type_32

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_artifact_packages_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_artifact_packages_create_validation_error.additional_properties = d
        return api_v1_artifact_packages_create_validation_error

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
