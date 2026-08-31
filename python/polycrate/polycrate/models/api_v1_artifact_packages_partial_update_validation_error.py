from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_artifact_packages_partial_update_annotations_error_component import (
        ApiV1ArtifactPackagesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_archived_at_error_component import (
        ApiV1ArtifactPackagesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_archived_by_error_component import (
        ApiV1ArtifactPackagesPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_archived_error_component import (
        ApiV1ArtifactPackagesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_archived_reason_error_component import (
        ApiV1ArtifactPackagesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_created_by_component_error_component import (
        ApiV1ArtifactPackagesPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_created_by_user_error_component import (
        ApiV1ArtifactPackagesPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_criticality_error_component import (
        ApiV1ArtifactPackagesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_debug_mode_error_component import (
        ApiV1ArtifactPackagesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_display_name_error_component import (
        ApiV1ArtifactPackagesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_kind_error_component import (
        ApiV1ArtifactPackagesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_labels_error_component import (
        ApiV1ArtifactPackagesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1ArtifactPackagesPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_managed_by_content_type_error_component import (
        ApiV1ArtifactPackagesPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_managed_by_object_id_error_component import (
        ApiV1ArtifactPackagesPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_modified_by_user_error_component import (
        ApiV1ArtifactPackagesPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_name_error_component import (
        ApiV1ArtifactPackagesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_non_field_errors_error_component import (
        ApiV1ArtifactPackagesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_platform_dns_record_created_error_component import (
        ApiV1ArtifactPackagesPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_platform_service_error_component import (
        ApiV1ArtifactPackagesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_provider_error_component import (
        ApiV1ArtifactPackagesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_provider_id_error_component import (
        ApiV1ArtifactPackagesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_provider_reference_error_component import (
        ApiV1ArtifactPackagesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_raw_data_error_component import (
        ApiV1ArtifactPackagesPartialUpdateRawDataErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_reconciliation_enabled_error_component import (
        ApiV1ArtifactPackagesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_sla_availability_error_component import (
        ApiV1ArtifactPackagesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_sla_target_error_component import (
        ApiV1ArtifactPackagesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_sla_window_days_error_component import (
        ApiV1ArtifactPackagesPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_slo_availability_error_component import (
        ApiV1ArtifactPackagesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_slo_target_error_component import (
        ApiV1ArtifactPackagesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_slo_window_days_error_component import (
        ApiV1ArtifactPackagesPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_target_availability_error_component import (
        ApiV1ArtifactPackagesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_partial_update_tolerations_error_component import (
        ApiV1ArtifactPackagesPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ArtifactPackagesPartialUpdateValidationError")


@_attrs_define
class ApiV1ArtifactPackagesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ArtifactPackagesPartialUpdateAnnotationsErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateArchivedAtErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateArchivedByErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateArchivedErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateArchivedReasonErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateCreatedByComponentErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateCreatedByUserErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateCriticalityErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateDebugModeErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateDisplayNameErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateKindErrorComponent | ApiV1ArtifactPackagesPartialUpdateLabelsErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateModifiedByUserErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateNameErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1ArtifactPackagesPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ArtifactPackagesPartialUpdatePlatformServiceErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateProviderErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateProviderIdErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateProviderReferenceErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateRawDataErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateSlaTargetErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateSlaWindowDaysErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateSloTargetErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateSloWindowDaysErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1ArtifactPackagesPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ArtifactPackagesPartialUpdateAnnotationsErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateArchivedAtErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateArchivedByErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateArchivedErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateArchivedReasonErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateCreatedByComponentErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateCreatedByUserErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateCriticalityErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateDebugModeErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateDisplayNameErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateKindErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateLabelsErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateModifiedByUserErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateNameErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1ArtifactPackagesPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ArtifactPackagesPartialUpdatePlatformServiceErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateProviderErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateProviderIdErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateProviderReferenceErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateRawDataErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateSlaTargetErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateSloTargetErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateSloWindowDaysErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1ArtifactPackagesPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_artifact_packages_partial_update_annotations_error_component import (
            ApiV1ArtifactPackagesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_archived_at_error_component import (
            ApiV1ArtifactPackagesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_archived_by_error_component import (
            ApiV1ArtifactPackagesPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_archived_error_component import (
            ApiV1ArtifactPackagesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_archived_reason_error_component import (
            ApiV1ArtifactPackagesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_created_by_component_error_component import (
            ApiV1ArtifactPackagesPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_criticality_error_component import (
            ApiV1ArtifactPackagesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_debug_mode_error_component import (
            ApiV1ArtifactPackagesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_display_name_error_component import (
            ApiV1ArtifactPackagesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_kind_error_component import (
            ApiV1ArtifactPackagesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_labels_error_component import (
            ApiV1ArtifactPackagesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactPackagesPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_managed_by_content_type_error_component import (
            ApiV1ArtifactPackagesPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_managed_by_object_id_error_component import (
            ApiV1ArtifactPackagesPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_modified_by_user_error_component import (
            ApiV1ArtifactPackagesPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_name_error_component import (
            ApiV1ArtifactPackagesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_non_field_errors_error_component import (
            ApiV1ArtifactPackagesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_platform_dns_record_created_error_component import (
            ApiV1ArtifactPackagesPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_platform_service_error_component import (
            ApiV1ArtifactPackagesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_provider_error_component import (
            ApiV1ArtifactPackagesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_provider_id_error_component import (
            ApiV1ArtifactPackagesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_provider_reference_error_component import (
            ApiV1ArtifactPackagesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_raw_data_error_component import (
            ApiV1ArtifactPackagesPartialUpdateRawDataErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_reconciliation_enabled_error_component import (
            ApiV1ArtifactPackagesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_sla_availability_error_component import (
            ApiV1ArtifactPackagesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_sla_target_error_component import (
            ApiV1ArtifactPackagesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_sla_window_days_error_component import (
            ApiV1ArtifactPackagesPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_slo_availability_error_component import (
            ApiV1ArtifactPackagesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_slo_target_error_component import (
            ApiV1ArtifactPackagesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_slo_window_days_error_component import (
            ApiV1ArtifactPackagesPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_target_availability_error_component import (
            ApiV1ArtifactPackagesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_tolerations_error_component import (
            ApiV1ArtifactPackagesPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactPackagesPartialUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateRawDataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesPartialUpdateModifiedByUserErrorComponent):
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
        from ..models.api_v1_artifact_packages_partial_update_annotations_error_component import (
            ApiV1ArtifactPackagesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_archived_at_error_component import (
            ApiV1ArtifactPackagesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_archived_by_error_component import (
            ApiV1ArtifactPackagesPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_archived_error_component import (
            ApiV1ArtifactPackagesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_archived_reason_error_component import (
            ApiV1ArtifactPackagesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_created_by_component_error_component import (
            ApiV1ArtifactPackagesPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_created_by_user_error_component import (
            ApiV1ArtifactPackagesPartialUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_criticality_error_component import (
            ApiV1ArtifactPackagesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_debug_mode_error_component import (
            ApiV1ArtifactPackagesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_display_name_error_component import (
            ApiV1ArtifactPackagesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_kind_error_component import (
            ApiV1ArtifactPackagesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_labels_error_component import (
            ApiV1ArtifactPackagesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactPackagesPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_managed_by_content_type_error_component import (
            ApiV1ArtifactPackagesPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_managed_by_object_id_error_component import (
            ApiV1ArtifactPackagesPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_modified_by_user_error_component import (
            ApiV1ArtifactPackagesPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_name_error_component import (
            ApiV1ArtifactPackagesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_non_field_errors_error_component import (
            ApiV1ArtifactPackagesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_platform_dns_record_created_error_component import (
            ApiV1ArtifactPackagesPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_platform_service_error_component import (
            ApiV1ArtifactPackagesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_provider_error_component import (
            ApiV1ArtifactPackagesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_provider_id_error_component import (
            ApiV1ArtifactPackagesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_provider_reference_error_component import (
            ApiV1ArtifactPackagesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_raw_data_error_component import (
            ApiV1ArtifactPackagesPartialUpdateRawDataErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_reconciliation_enabled_error_component import (
            ApiV1ArtifactPackagesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_sla_availability_error_component import (
            ApiV1ArtifactPackagesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_sla_target_error_component import (
            ApiV1ArtifactPackagesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_sla_window_days_error_component import (
            ApiV1ArtifactPackagesPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_slo_availability_error_component import (
            ApiV1ArtifactPackagesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_slo_target_error_component import (
            ApiV1ArtifactPackagesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_slo_window_days_error_component import (
            ApiV1ArtifactPackagesPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_target_availability_error_component import (
            ApiV1ArtifactPackagesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_partial_update_tolerations_error_component import (
            ApiV1ArtifactPackagesPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ArtifactPackagesPartialUpdateAnnotationsErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateArchivedAtErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateArchivedByErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateArchivedErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateArchivedReasonErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateCreatedByComponentErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateCreatedByUserErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateCriticalityErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateDebugModeErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateDisplayNameErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateKindErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateLabelsErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateModifiedByUserErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateNameErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1ArtifactPackagesPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ArtifactPackagesPartialUpdatePlatformServiceErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateProviderErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateProviderIdErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateProviderReferenceErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateRawDataErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateSlaTargetErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateSloTargetErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateSloWindowDaysErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1ArtifactPackagesPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_0 = (
                        ApiV1ArtifactPackagesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_1 = (
                        ApiV1ArtifactPackagesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_2 = (
                        ApiV1ArtifactPackagesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_3 = (
                        ApiV1ArtifactPackagesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_4 = (
                        ApiV1ArtifactPackagesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_5 = (
                        ApiV1ArtifactPackagesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_6 = (
                        ApiV1ArtifactPackagesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_7 = (
                        ApiV1ArtifactPackagesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_8 = (
                        ApiV1ArtifactPackagesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_9 = (
                        ApiV1ArtifactPackagesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_10 = (
                        ApiV1ArtifactPackagesPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_11 = (
                        ApiV1ArtifactPackagesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_12 = (
                        ApiV1ArtifactPackagesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_13 = (
                        ApiV1ArtifactPackagesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_14 = (
                        ApiV1ArtifactPackagesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_15 = (
                        ApiV1ArtifactPackagesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_16 = (
                        ApiV1ArtifactPackagesPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_17 = (
                        ApiV1ArtifactPackagesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_18 = (
                        ApiV1ArtifactPackagesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_19 = (
                        ApiV1ArtifactPackagesPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_20 = (
                        ApiV1ArtifactPackagesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_21 = (
                        ApiV1ArtifactPackagesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_22 = (
                        ApiV1ArtifactPackagesPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_23 = (
                        ApiV1ArtifactPackagesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_24 = (
                        ApiV1ArtifactPackagesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_25 = (
                        ApiV1ArtifactPackagesPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_26 = (
                        ApiV1ArtifactPackagesPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_27 = (
                        ApiV1ArtifactPackagesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_28 = (
                        ApiV1ArtifactPackagesPartialUpdateRawDataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_29 = (
                        ApiV1ArtifactPackagesPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_30 = (
                        ApiV1ArtifactPackagesPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_partial_update_error_type_31 = (
                        ApiV1ArtifactPackagesPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_artifact_packages_partial_update_error_type_32 = (
                    ApiV1ArtifactPackagesPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_artifact_packages_partial_update_error_type_32

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_artifact_packages_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_artifact_packages_partial_update_validation_error.additional_properties = d
        return api_v1_artifact_packages_partial_update_validation_error

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
