from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_cves_partial_update_actual_availability_error_component import (
        ApiV1CvesPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_annotations_error_component import (
        ApiV1CvesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_archived_at_error_component import (
        ApiV1CvesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_archived_by_error_component import (
        ApiV1CvesPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_archived_error_component import (
        ApiV1CvesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_archived_reason_error_component import (
        ApiV1CvesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_created_by_component_error_component import (
        ApiV1CvesPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_created_by_user_error_component import (
        ApiV1CvesPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_criticality_error_component import (
        ApiV1CvesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_cve_id_error_component import ApiV1CvesPartialUpdateCveIdErrorComponent
    from ..models.api_v1_cves_partial_update_cvss_score_error_component import (
        ApiV1CvesPartialUpdateCvssScoreErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_cvss_vector_error_component import (
        ApiV1CvesPartialUpdateCvssVectorErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_debug_mode_error_component import (
        ApiV1CvesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_description_error_component import (
        ApiV1CvesPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_discovery_enabled_error_component import (
        ApiV1CvesPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_display_name_error_component import (
        ApiV1CvesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_kind_error_component import ApiV1CvesPartialUpdateKindErrorComponent
    from ..models.api_v1_cves_partial_update_labels_error_component import ApiV1CvesPartialUpdateLabelsErrorComponent
    from ..models.api_v1_cves_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1CvesPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_managed_by_content_type_error_component import (
        ApiV1CvesPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_managed_by_object_id_error_component import (
        ApiV1CvesPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_modified_at_error_component import (
        ApiV1CvesPartialUpdateModifiedAtErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_modified_by_user_error_component import (
        ApiV1CvesPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_name_error_component import ApiV1CvesPartialUpdateNameErrorComponent
    from ..models.api_v1_cves_partial_update_non_field_errors_error_component import (
        ApiV1CvesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_platform_dns_record_created_error_component import (
        ApiV1CvesPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_platform_service_error_component import (
        ApiV1CvesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_provider_error_component import (
        ApiV1CvesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_provider_id_error_component import (
        ApiV1CvesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_provider_reference_error_component import (
        ApiV1CvesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_published_at_error_component import (
        ApiV1CvesPartialUpdatePublishedAtErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_reconciliation_enabled_error_component import (
        ApiV1CvesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_scope_error_component import ApiV1CvesPartialUpdateScopeErrorComponent
    from ..models.api_v1_cves_partial_update_severity_error_component import (
        ApiV1CvesPartialUpdateSeverityErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_sla_availability_error_component import (
        ApiV1CvesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_sla_target_error_component import (
        ApiV1CvesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_sla_window_days_error_component import (
        ApiV1CvesPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_slo_availability_error_component import (
        ApiV1CvesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_slo_target_error_component import (
        ApiV1CvesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_slo_window_days_error_component import (
        ApiV1CvesPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_status_error_component import ApiV1CvesPartialUpdateStatusErrorComponent
    from ..models.api_v1_cves_partial_update_target_availability_error_component import (
        ApiV1CvesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_partial_update_title_error_component import ApiV1CvesPartialUpdateTitleErrorComponent


T = TypeVar("T", bound="ApiV1CvesPartialUpdateValidationError")


@_attrs_define
class ApiV1CvesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CvesPartialUpdateActualAvailabilityErrorComponent |
            ApiV1CvesPartialUpdateAnnotationsErrorComponent | ApiV1CvesPartialUpdateArchivedAtErrorComponent |
            ApiV1CvesPartialUpdateArchivedByErrorComponent | ApiV1CvesPartialUpdateArchivedErrorComponent |
            ApiV1CvesPartialUpdateArchivedReasonErrorComponent | ApiV1CvesPartialUpdateCreatedByComponentErrorComponent |
            ApiV1CvesPartialUpdateCreatedByUserErrorComponent | ApiV1CvesPartialUpdateCriticalityErrorComponent |
            ApiV1CvesPartialUpdateCveIdErrorComponent | ApiV1CvesPartialUpdateCvssScoreErrorComponent |
            ApiV1CvesPartialUpdateCvssVectorErrorComponent | ApiV1CvesPartialUpdateDebugModeErrorComponent |
            ApiV1CvesPartialUpdateDescriptionErrorComponent | ApiV1CvesPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1CvesPartialUpdateDisplayNameErrorComponent | ApiV1CvesPartialUpdateKindErrorComponent |
            ApiV1CvesPartialUpdateLabelsErrorComponent |
            ApiV1CvesPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1CvesPartialUpdateManagedByContentTypeErrorComponent | ApiV1CvesPartialUpdateManagedByObjectIdErrorComponent
            | ApiV1CvesPartialUpdateModifiedAtErrorComponent | ApiV1CvesPartialUpdateModifiedByUserErrorComponent |
            ApiV1CvesPartialUpdateNameErrorComponent | ApiV1CvesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1CvesPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1CvesPartialUpdatePlatformServiceErrorComponent | ApiV1CvesPartialUpdateProviderErrorComponent |
            ApiV1CvesPartialUpdateProviderIdErrorComponent | ApiV1CvesPartialUpdateProviderReferenceErrorComponent |
            ApiV1CvesPartialUpdatePublishedAtErrorComponent | ApiV1CvesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1CvesPartialUpdateScopeErrorComponent | ApiV1CvesPartialUpdateSeverityErrorComponent |
            ApiV1CvesPartialUpdateSlaAvailabilityErrorComponent | ApiV1CvesPartialUpdateSlaTargetErrorComponent |
            ApiV1CvesPartialUpdateSlaWindowDaysErrorComponent | ApiV1CvesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1CvesPartialUpdateSloTargetErrorComponent | ApiV1CvesPartialUpdateSloWindowDaysErrorComponent |
            ApiV1CvesPartialUpdateStatusErrorComponent | ApiV1CvesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1CvesPartialUpdateTitleErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CvesPartialUpdateActualAvailabilityErrorComponent
        | ApiV1CvesPartialUpdateAnnotationsErrorComponent
        | ApiV1CvesPartialUpdateArchivedAtErrorComponent
        | ApiV1CvesPartialUpdateArchivedByErrorComponent
        | ApiV1CvesPartialUpdateArchivedErrorComponent
        | ApiV1CvesPartialUpdateArchivedReasonErrorComponent
        | ApiV1CvesPartialUpdateCreatedByComponentErrorComponent
        | ApiV1CvesPartialUpdateCreatedByUserErrorComponent
        | ApiV1CvesPartialUpdateCriticalityErrorComponent
        | ApiV1CvesPartialUpdateCveIdErrorComponent
        | ApiV1CvesPartialUpdateCvssScoreErrorComponent
        | ApiV1CvesPartialUpdateCvssVectorErrorComponent
        | ApiV1CvesPartialUpdateDebugModeErrorComponent
        | ApiV1CvesPartialUpdateDescriptionErrorComponent
        | ApiV1CvesPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1CvesPartialUpdateDisplayNameErrorComponent
        | ApiV1CvesPartialUpdateKindErrorComponent
        | ApiV1CvesPartialUpdateLabelsErrorComponent
        | ApiV1CvesPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1CvesPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1CvesPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1CvesPartialUpdateModifiedAtErrorComponent
        | ApiV1CvesPartialUpdateModifiedByUserErrorComponent
        | ApiV1CvesPartialUpdateNameErrorComponent
        | ApiV1CvesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1CvesPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1CvesPartialUpdatePlatformServiceErrorComponent
        | ApiV1CvesPartialUpdateProviderErrorComponent
        | ApiV1CvesPartialUpdateProviderIdErrorComponent
        | ApiV1CvesPartialUpdateProviderReferenceErrorComponent
        | ApiV1CvesPartialUpdatePublishedAtErrorComponent
        | ApiV1CvesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1CvesPartialUpdateScopeErrorComponent
        | ApiV1CvesPartialUpdateSeverityErrorComponent
        | ApiV1CvesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1CvesPartialUpdateSlaTargetErrorComponent
        | ApiV1CvesPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1CvesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1CvesPartialUpdateSloTargetErrorComponent
        | ApiV1CvesPartialUpdateSloWindowDaysErrorComponent
        | ApiV1CvesPartialUpdateStatusErrorComponent
        | ApiV1CvesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1CvesPartialUpdateTitleErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_cves_partial_update_actual_availability_error_component import (
            ApiV1CvesPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_annotations_error_component import (
            ApiV1CvesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_archived_at_error_component import (
            ApiV1CvesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_archived_by_error_component import (
            ApiV1CvesPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_archived_error_component import (
            ApiV1CvesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_archived_reason_error_component import (
            ApiV1CvesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_created_by_component_error_component import (
            ApiV1CvesPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_criticality_error_component import (
            ApiV1CvesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_cve_id_error_component import ApiV1CvesPartialUpdateCveIdErrorComponent
        from ..models.api_v1_cves_partial_update_cvss_score_error_component import (
            ApiV1CvesPartialUpdateCvssScoreErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_cvss_vector_error_component import (
            ApiV1CvesPartialUpdateCvssVectorErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_debug_mode_error_component import (
            ApiV1CvesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_description_error_component import (
            ApiV1CvesPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_discovery_enabled_error_component import (
            ApiV1CvesPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_display_name_error_component import (
            ApiV1CvesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_kind_error_component import ApiV1CvesPartialUpdateKindErrorComponent
        from ..models.api_v1_cves_partial_update_labels_error_component import (
            ApiV1CvesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1CvesPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_managed_by_content_type_error_component import (
            ApiV1CvesPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_managed_by_object_id_error_component import (
            ApiV1CvesPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_modified_at_error_component import (
            ApiV1CvesPartialUpdateModifiedAtErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_modified_by_user_error_component import (
            ApiV1CvesPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_name_error_component import ApiV1CvesPartialUpdateNameErrorComponent
        from ..models.api_v1_cves_partial_update_non_field_errors_error_component import (
            ApiV1CvesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_platform_dns_record_created_error_component import (
            ApiV1CvesPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_platform_service_error_component import (
            ApiV1CvesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_provider_error_component import (
            ApiV1CvesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_provider_id_error_component import (
            ApiV1CvesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_provider_reference_error_component import (
            ApiV1CvesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_published_at_error_component import (
            ApiV1CvesPartialUpdatePublishedAtErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_reconciliation_enabled_error_component import (
            ApiV1CvesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_scope_error_component import ApiV1CvesPartialUpdateScopeErrorComponent
        from ..models.api_v1_cves_partial_update_severity_error_component import (
            ApiV1CvesPartialUpdateSeverityErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_sla_availability_error_component import (
            ApiV1CvesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_sla_target_error_component import (
            ApiV1CvesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_sla_window_days_error_component import (
            ApiV1CvesPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_slo_availability_error_component import (
            ApiV1CvesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_slo_target_error_component import (
            ApiV1CvesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_slo_window_days_error_component import (
            ApiV1CvesPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_status_error_component import (
            ApiV1CvesPartialUpdateStatusErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_target_availability_error_component import (
            ApiV1CvesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_title_error_component import ApiV1CvesPartialUpdateTitleErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CvesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateCveIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateTitleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdatePublishedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateModifiedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateCvssScoreErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateCvssVectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateSeverityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesPartialUpdateModifiedByUserErrorComponent):
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
        from ..models.api_v1_cves_partial_update_actual_availability_error_component import (
            ApiV1CvesPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_annotations_error_component import (
            ApiV1CvesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_archived_at_error_component import (
            ApiV1CvesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_archived_by_error_component import (
            ApiV1CvesPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_archived_error_component import (
            ApiV1CvesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_archived_reason_error_component import (
            ApiV1CvesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_created_by_component_error_component import (
            ApiV1CvesPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_created_by_user_error_component import (
            ApiV1CvesPartialUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_criticality_error_component import (
            ApiV1CvesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_cve_id_error_component import ApiV1CvesPartialUpdateCveIdErrorComponent
        from ..models.api_v1_cves_partial_update_cvss_score_error_component import (
            ApiV1CvesPartialUpdateCvssScoreErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_cvss_vector_error_component import (
            ApiV1CvesPartialUpdateCvssVectorErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_debug_mode_error_component import (
            ApiV1CvesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_description_error_component import (
            ApiV1CvesPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_discovery_enabled_error_component import (
            ApiV1CvesPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_display_name_error_component import (
            ApiV1CvesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_kind_error_component import ApiV1CvesPartialUpdateKindErrorComponent
        from ..models.api_v1_cves_partial_update_labels_error_component import (
            ApiV1CvesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1CvesPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_managed_by_content_type_error_component import (
            ApiV1CvesPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_managed_by_object_id_error_component import (
            ApiV1CvesPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_modified_at_error_component import (
            ApiV1CvesPartialUpdateModifiedAtErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_modified_by_user_error_component import (
            ApiV1CvesPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_name_error_component import ApiV1CvesPartialUpdateNameErrorComponent
        from ..models.api_v1_cves_partial_update_non_field_errors_error_component import (
            ApiV1CvesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_platform_dns_record_created_error_component import (
            ApiV1CvesPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_platform_service_error_component import (
            ApiV1CvesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_provider_error_component import (
            ApiV1CvesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_provider_id_error_component import (
            ApiV1CvesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_provider_reference_error_component import (
            ApiV1CvesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_published_at_error_component import (
            ApiV1CvesPartialUpdatePublishedAtErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_reconciliation_enabled_error_component import (
            ApiV1CvesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_scope_error_component import ApiV1CvesPartialUpdateScopeErrorComponent
        from ..models.api_v1_cves_partial_update_severity_error_component import (
            ApiV1CvesPartialUpdateSeverityErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_sla_availability_error_component import (
            ApiV1CvesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_sla_target_error_component import (
            ApiV1CvesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_sla_window_days_error_component import (
            ApiV1CvesPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_slo_availability_error_component import (
            ApiV1CvesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_slo_target_error_component import (
            ApiV1CvesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_slo_window_days_error_component import (
            ApiV1CvesPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_status_error_component import (
            ApiV1CvesPartialUpdateStatusErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_target_availability_error_component import (
            ApiV1CvesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_cves_partial_update_title_error_component import ApiV1CvesPartialUpdateTitleErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CvesPartialUpdateActualAvailabilityErrorComponent
                | ApiV1CvesPartialUpdateAnnotationsErrorComponent
                | ApiV1CvesPartialUpdateArchivedAtErrorComponent
                | ApiV1CvesPartialUpdateArchivedByErrorComponent
                | ApiV1CvesPartialUpdateArchivedErrorComponent
                | ApiV1CvesPartialUpdateArchivedReasonErrorComponent
                | ApiV1CvesPartialUpdateCreatedByComponentErrorComponent
                | ApiV1CvesPartialUpdateCreatedByUserErrorComponent
                | ApiV1CvesPartialUpdateCriticalityErrorComponent
                | ApiV1CvesPartialUpdateCveIdErrorComponent
                | ApiV1CvesPartialUpdateCvssScoreErrorComponent
                | ApiV1CvesPartialUpdateCvssVectorErrorComponent
                | ApiV1CvesPartialUpdateDebugModeErrorComponent
                | ApiV1CvesPartialUpdateDescriptionErrorComponent
                | ApiV1CvesPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1CvesPartialUpdateDisplayNameErrorComponent
                | ApiV1CvesPartialUpdateKindErrorComponent
                | ApiV1CvesPartialUpdateLabelsErrorComponent
                | ApiV1CvesPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1CvesPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1CvesPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1CvesPartialUpdateModifiedAtErrorComponent
                | ApiV1CvesPartialUpdateModifiedByUserErrorComponent
                | ApiV1CvesPartialUpdateNameErrorComponent
                | ApiV1CvesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1CvesPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1CvesPartialUpdatePlatformServiceErrorComponent
                | ApiV1CvesPartialUpdateProviderErrorComponent
                | ApiV1CvesPartialUpdateProviderIdErrorComponent
                | ApiV1CvesPartialUpdateProviderReferenceErrorComponent
                | ApiV1CvesPartialUpdatePublishedAtErrorComponent
                | ApiV1CvesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1CvesPartialUpdateScopeErrorComponent
                | ApiV1CvesPartialUpdateSeverityErrorComponent
                | ApiV1CvesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1CvesPartialUpdateSlaTargetErrorComponent
                | ApiV1CvesPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1CvesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1CvesPartialUpdateSloTargetErrorComponent
                | ApiV1CvesPartialUpdateSloWindowDaysErrorComponent
                | ApiV1CvesPartialUpdateStatusErrorComponent
                | ApiV1CvesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1CvesPartialUpdateTitleErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_0 = (
                        ApiV1CvesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_1 = (
                        ApiV1CvesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_2 = (
                        ApiV1CvesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_3 = (
                        ApiV1CvesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_4 = (
                        ApiV1CvesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_5 = (
                        ApiV1CvesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_6 = (
                        ApiV1CvesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_7 = (
                        ApiV1CvesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_8 = (
                        ApiV1CvesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_9 = (
                        ApiV1CvesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_10 = (
                        ApiV1CvesPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_11 = (
                        ApiV1CvesPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_12 = (
                        ApiV1CvesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_13 = (
                        ApiV1CvesPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_14 = (
                        ApiV1CvesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_15 = (
                        ApiV1CvesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_16 = (
                        ApiV1CvesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_17 = (
                        ApiV1CvesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_18 = (
                        ApiV1CvesPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_19 = (
                        ApiV1CvesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_20 = (
                        ApiV1CvesPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_21 = (
                        ApiV1CvesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_22 = (
                        ApiV1CvesPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_23 = (
                        ApiV1CvesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_24 = (
                        ApiV1CvesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_25 = (
                        ApiV1CvesPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_26 = (
                        ApiV1CvesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_27 = (
                        ApiV1CvesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_28 = (
                        ApiV1CvesPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_29 = (
                        ApiV1CvesPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_30 = (
                        ApiV1CvesPartialUpdateCveIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_31 = (
                        ApiV1CvesPartialUpdateTitleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_32 = (
                        ApiV1CvesPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_33 = (
                        ApiV1CvesPartialUpdatePublishedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_34 = (
                        ApiV1CvesPartialUpdateModifiedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_35 = (
                        ApiV1CvesPartialUpdateCvssScoreErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_36 = (
                        ApiV1CvesPartialUpdateCvssVectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_37 = (
                        ApiV1CvesPartialUpdateSeverityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_38 = (
                        ApiV1CvesPartialUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_39 = (
                        ApiV1CvesPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_40 = (
                        ApiV1CvesPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_partial_update_error_type_41 = (
                        ApiV1CvesPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_cves_partial_update_error_type_42 = (
                    ApiV1CvesPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_cves_partial_update_error_type_42

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_cves_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_cves_partial_update_validation_error.additional_properties = d
        return api_v1_cves_partial_update_validation_error

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
