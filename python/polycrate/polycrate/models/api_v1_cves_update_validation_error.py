from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_cves_update_actual_availability_error_component import (
        ApiV1CvesUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_update_annotations_error_component import ApiV1CvesUpdateAnnotationsErrorComponent
    from ..models.api_v1_cves_update_archived_at_error_component import ApiV1CvesUpdateArchivedAtErrorComponent
    from ..models.api_v1_cves_update_archived_by_error_component import ApiV1CvesUpdateArchivedByErrorComponent
    from ..models.api_v1_cves_update_archived_error_component import ApiV1CvesUpdateArchivedErrorComponent
    from ..models.api_v1_cves_update_archived_reason_error_component import ApiV1CvesUpdateArchivedReasonErrorComponent
    from ..models.api_v1_cves_update_created_by_component_error_component import (
        ApiV1CvesUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_cves_update_created_by_user_error_component import ApiV1CvesUpdateCreatedByUserErrorComponent
    from ..models.api_v1_cves_update_criticality_error_component import ApiV1CvesUpdateCriticalityErrorComponent
    from ..models.api_v1_cves_update_cve_id_error_component import ApiV1CvesUpdateCveIdErrorComponent
    from ..models.api_v1_cves_update_cvss_score_error_component import ApiV1CvesUpdateCvssScoreErrorComponent
    from ..models.api_v1_cves_update_cvss_vector_error_component import ApiV1CvesUpdateCvssVectorErrorComponent
    from ..models.api_v1_cves_update_debug_mode_error_component import ApiV1CvesUpdateDebugModeErrorComponent
    from ..models.api_v1_cves_update_description_error_component import ApiV1CvesUpdateDescriptionErrorComponent
    from ..models.api_v1_cves_update_discovery_enabled_error_component import (
        ApiV1CvesUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_cves_update_display_name_error_component import ApiV1CvesUpdateDisplayNameErrorComponent
    from ..models.api_v1_cves_update_kind_error_component import ApiV1CvesUpdateKindErrorComponent
    from ..models.api_v1_cves_update_labels_error_component import ApiV1CvesUpdateLabelsErrorComponent
    from ..models.api_v1_cves_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1CvesUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_cves_update_managed_by_content_type_error_component import (
        ApiV1CvesUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_cves_update_managed_by_object_id_error_component import (
        ApiV1CvesUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_cves_update_modified_at_error_component import ApiV1CvesUpdateModifiedAtErrorComponent
    from ..models.api_v1_cves_update_modified_by_user_error_component import ApiV1CvesUpdateModifiedByUserErrorComponent
    from ..models.api_v1_cves_update_name_error_component import ApiV1CvesUpdateNameErrorComponent
    from ..models.api_v1_cves_update_non_field_errors_error_component import ApiV1CvesUpdateNonFieldErrorsErrorComponent
    from ..models.api_v1_cves_update_platform_dns_record_created_error_component import (
        ApiV1CvesUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_cves_update_platform_service_error_component import (
        ApiV1CvesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_cves_update_provider_error_component import ApiV1CvesUpdateProviderErrorComponent
    from ..models.api_v1_cves_update_provider_id_error_component import ApiV1CvesUpdateProviderIdErrorComponent
    from ..models.api_v1_cves_update_provider_reference_error_component import (
        ApiV1CvesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_cves_update_published_at_error_component import ApiV1CvesUpdatePublishedAtErrorComponent
    from ..models.api_v1_cves_update_reconciliation_enabled_error_component import (
        ApiV1CvesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_cves_update_scope_error_component import ApiV1CvesUpdateScopeErrorComponent
    from ..models.api_v1_cves_update_severity_error_component import ApiV1CvesUpdateSeverityErrorComponent
    from ..models.api_v1_cves_update_sla_availability_error_component import (
        ApiV1CvesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_update_sla_target_error_component import ApiV1CvesUpdateSlaTargetErrorComponent
    from ..models.api_v1_cves_update_sla_window_days_error_component import ApiV1CvesUpdateSlaWindowDaysErrorComponent
    from ..models.api_v1_cves_update_slo_availability_error_component import (
        ApiV1CvesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_update_slo_target_error_component import ApiV1CvesUpdateSloTargetErrorComponent
    from ..models.api_v1_cves_update_slo_window_days_error_component import ApiV1CvesUpdateSloWindowDaysErrorComponent
    from ..models.api_v1_cves_update_status_error_component import ApiV1CvesUpdateStatusErrorComponent
    from ..models.api_v1_cves_update_target_availability_error_component import (
        ApiV1CvesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_update_title_error_component import ApiV1CvesUpdateTitleErrorComponent


T = TypeVar("T", bound="ApiV1CvesUpdateValidationError")


@_attrs_define
class ApiV1CvesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CvesUpdateActualAvailabilityErrorComponent | ApiV1CvesUpdateAnnotationsErrorComponent |
            ApiV1CvesUpdateArchivedAtErrorComponent | ApiV1CvesUpdateArchivedByErrorComponent |
            ApiV1CvesUpdateArchivedErrorComponent | ApiV1CvesUpdateArchivedReasonErrorComponent |
            ApiV1CvesUpdateCreatedByComponentErrorComponent | ApiV1CvesUpdateCreatedByUserErrorComponent |
            ApiV1CvesUpdateCriticalityErrorComponent | ApiV1CvesUpdateCveIdErrorComponent |
            ApiV1CvesUpdateCvssScoreErrorComponent | ApiV1CvesUpdateCvssVectorErrorComponent |
            ApiV1CvesUpdateDebugModeErrorComponent | ApiV1CvesUpdateDescriptionErrorComponent |
            ApiV1CvesUpdateDiscoveryEnabledErrorComponent | ApiV1CvesUpdateDisplayNameErrorComponent |
            ApiV1CvesUpdateKindErrorComponent | ApiV1CvesUpdateLabelsErrorComponent |
            ApiV1CvesUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1CvesUpdateManagedByContentTypeErrorComponent | ApiV1CvesUpdateManagedByObjectIdErrorComponent |
            ApiV1CvesUpdateModifiedAtErrorComponent | ApiV1CvesUpdateModifiedByUserErrorComponent |
            ApiV1CvesUpdateNameErrorComponent | ApiV1CvesUpdateNonFieldErrorsErrorComponent |
            ApiV1CvesUpdatePlatformDnsRecordCreatedErrorComponent | ApiV1CvesUpdatePlatformServiceErrorComponent |
            ApiV1CvesUpdateProviderErrorComponent | ApiV1CvesUpdateProviderIdErrorComponent |
            ApiV1CvesUpdateProviderReferenceErrorComponent | ApiV1CvesUpdatePublishedAtErrorComponent |
            ApiV1CvesUpdateReconciliationEnabledErrorComponent | ApiV1CvesUpdateScopeErrorComponent |
            ApiV1CvesUpdateSeverityErrorComponent | ApiV1CvesUpdateSlaAvailabilityErrorComponent |
            ApiV1CvesUpdateSlaTargetErrorComponent | ApiV1CvesUpdateSlaWindowDaysErrorComponent |
            ApiV1CvesUpdateSloAvailabilityErrorComponent | ApiV1CvesUpdateSloTargetErrorComponent |
            ApiV1CvesUpdateSloWindowDaysErrorComponent | ApiV1CvesUpdateStatusErrorComponent |
            ApiV1CvesUpdateTargetAvailabilityErrorComponent | ApiV1CvesUpdateTitleErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CvesUpdateActualAvailabilityErrorComponent
        | ApiV1CvesUpdateAnnotationsErrorComponent
        | ApiV1CvesUpdateArchivedAtErrorComponent
        | ApiV1CvesUpdateArchivedByErrorComponent
        | ApiV1CvesUpdateArchivedErrorComponent
        | ApiV1CvesUpdateArchivedReasonErrorComponent
        | ApiV1CvesUpdateCreatedByComponentErrorComponent
        | ApiV1CvesUpdateCreatedByUserErrorComponent
        | ApiV1CvesUpdateCriticalityErrorComponent
        | ApiV1CvesUpdateCveIdErrorComponent
        | ApiV1CvesUpdateCvssScoreErrorComponent
        | ApiV1CvesUpdateCvssVectorErrorComponent
        | ApiV1CvesUpdateDebugModeErrorComponent
        | ApiV1CvesUpdateDescriptionErrorComponent
        | ApiV1CvesUpdateDiscoveryEnabledErrorComponent
        | ApiV1CvesUpdateDisplayNameErrorComponent
        | ApiV1CvesUpdateKindErrorComponent
        | ApiV1CvesUpdateLabelsErrorComponent
        | ApiV1CvesUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1CvesUpdateManagedByContentTypeErrorComponent
        | ApiV1CvesUpdateManagedByObjectIdErrorComponent
        | ApiV1CvesUpdateModifiedAtErrorComponent
        | ApiV1CvesUpdateModifiedByUserErrorComponent
        | ApiV1CvesUpdateNameErrorComponent
        | ApiV1CvesUpdateNonFieldErrorsErrorComponent
        | ApiV1CvesUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1CvesUpdatePlatformServiceErrorComponent
        | ApiV1CvesUpdateProviderErrorComponent
        | ApiV1CvesUpdateProviderIdErrorComponent
        | ApiV1CvesUpdateProviderReferenceErrorComponent
        | ApiV1CvesUpdatePublishedAtErrorComponent
        | ApiV1CvesUpdateReconciliationEnabledErrorComponent
        | ApiV1CvesUpdateScopeErrorComponent
        | ApiV1CvesUpdateSeverityErrorComponent
        | ApiV1CvesUpdateSlaAvailabilityErrorComponent
        | ApiV1CvesUpdateSlaTargetErrorComponent
        | ApiV1CvesUpdateSlaWindowDaysErrorComponent
        | ApiV1CvesUpdateSloAvailabilityErrorComponent
        | ApiV1CvesUpdateSloTargetErrorComponent
        | ApiV1CvesUpdateSloWindowDaysErrorComponent
        | ApiV1CvesUpdateStatusErrorComponent
        | ApiV1CvesUpdateTargetAvailabilityErrorComponent
        | ApiV1CvesUpdateTitleErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_cves_update_actual_availability_error_component import (
            ApiV1CvesUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_annotations_error_component import (
            ApiV1CvesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_archived_at_error_component import (
            ApiV1CvesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_archived_by_error_component import (
            ApiV1CvesUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_archived_error_component import (
            ApiV1CvesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_archived_reason_error_component import (
            ApiV1CvesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_created_by_component_error_component import (
            ApiV1CvesUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_criticality_error_component import (
            ApiV1CvesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_cve_id_error_component import (
            ApiV1CvesUpdateCveIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_cvss_score_error_component import (
            ApiV1CvesUpdateCvssScoreErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_cvss_vector_error_component import (
            ApiV1CvesUpdateCvssVectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_debug_mode_error_component import (
            ApiV1CvesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_description_error_component import (
            ApiV1CvesUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_discovery_enabled_error_component import (
            ApiV1CvesUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_display_name_error_component import (
            ApiV1CvesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_kind_error_component import ApiV1CvesUpdateKindErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_update_labels_error_component import (
            ApiV1CvesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1CvesUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_managed_by_content_type_error_component import (
            ApiV1CvesUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_managed_by_object_id_error_component import (
            ApiV1CvesUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_modified_at_error_component import (
            ApiV1CvesUpdateModifiedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_modified_by_user_error_component import (
            ApiV1CvesUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_name_error_component import ApiV1CvesUpdateNameErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_update_non_field_errors_error_component import (
            ApiV1CvesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_platform_dns_record_created_error_component import (
            ApiV1CvesUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_platform_service_error_component import (
            ApiV1CvesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_provider_error_component import (
            ApiV1CvesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_provider_id_error_component import (
            ApiV1CvesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_provider_reference_error_component import (
            ApiV1CvesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_published_at_error_component import (
            ApiV1CvesUpdatePublishedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_reconciliation_enabled_error_component import (
            ApiV1CvesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_scope_error_component import (
            ApiV1CvesUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_severity_error_component import (
            ApiV1CvesUpdateSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_sla_availability_error_component import (
            ApiV1CvesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_sla_target_error_component import (
            ApiV1CvesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_sla_window_days_error_component import (
            ApiV1CvesUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_slo_availability_error_component import (
            ApiV1CvesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_slo_target_error_component import (
            ApiV1CvesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_slo_window_days_error_component import (
            ApiV1CvesUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_status_error_component import (
            ApiV1CvesUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_target_availability_error_component import (
            ApiV1CvesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_title_error_component import (
            ApiV1CvesUpdateTitleErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CvesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateCveIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateTitleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdatePublishedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateModifiedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateCvssScoreErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateCvssVectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateSeverityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesUpdateModifiedByUserErrorComponent):
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
        from ..models.api_v1_cves_update_actual_availability_error_component import (
            ApiV1CvesUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_annotations_error_component import (
            ApiV1CvesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_archived_at_error_component import (
            ApiV1CvesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_archived_by_error_component import (
            ApiV1CvesUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_archived_error_component import (
            ApiV1CvesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_archived_reason_error_component import (
            ApiV1CvesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_created_by_component_error_component import (
            ApiV1CvesUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_created_by_user_error_component import (
            ApiV1CvesUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_criticality_error_component import (
            ApiV1CvesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_cve_id_error_component import (
            ApiV1CvesUpdateCveIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_cvss_score_error_component import (
            ApiV1CvesUpdateCvssScoreErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_cvss_vector_error_component import (
            ApiV1CvesUpdateCvssVectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_debug_mode_error_component import (
            ApiV1CvesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_description_error_component import (
            ApiV1CvesUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_discovery_enabled_error_component import (
            ApiV1CvesUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_display_name_error_component import (
            ApiV1CvesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_kind_error_component import ApiV1CvesUpdateKindErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_update_labels_error_component import (
            ApiV1CvesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1CvesUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_managed_by_content_type_error_component import (
            ApiV1CvesUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_managed_by_object_id_error_component import (
            ApiV1CvesUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_modified_at_error_component import (
            ApiV1CvesUpdateModifiedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_modified_by_user_error_component import (
            ApiV1CvesUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_name_error_component import ApiV1CvesUpdateNameErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_update_non_field_errors_error_component import (
            ApiV1CvesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_platform_dns_record_created_error_component import (
            ApiV1CvesUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_platform_service_error_component import (
            ApiV1CvesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_provider_error_component import (
            ApiV1CvesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_provider_id_error_component import (
            ApiV1CvesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_provider_reference_error_component import (
            ApiV1CvesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_published_at_error_component import (
            ApiV1CvesUpdatePublishedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_reconciliation_enabled_error_component import (
            ApiV1CvesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_scope_error_component import (
            ApiV1CvesUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_severity_error_component import (
            ApiV1CvesUpdateSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_sla_availability_error_component import (
            ApiV1CvesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_sla_target_error_component import (
            ApiV1CvesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_sla_window_days_error_component import (
            ApiV1CvesUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_slo_availability_error_component import (
            ApiV1CvesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_slo_target_error_component import (
            ApiV1CvesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_slo_window_days_error_component import (
            ApiV1CvesUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_status_error_component import (
            ApiV1CvesUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_target_availability_error_component import (
            ApiV1CvesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_update_title_error_component import (
            ApiV1CvesUpdateTitleErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CvesUpdateActualAvailabilityErrorComponent
                | ApiV1CvesUpdateAnnotationsErrorComponent
                | ApiV1CvesUpdateArchivedAtErrorComponent
                | ApiV1CvesUpdateArchivedByErrorComponent
                | ApiV1CvesUpdateArchivedErrorComponent
                | ApiV1CvesUpdateArchivedReasonErrorComponent
                | ApiV1CvesUpdateCreatedByComponentErrorComponent
                | ApiV1CvesUpdateCreatedByUserErrorComponent
                | ApiV1CvesUpdateCriticalityErrorComponent
                | ApiV1CvesUpdateCveIdErrorComponent
                | ApiV1CvesUpdateCvssScoreErrorComponent
                | ApiV1CvesUpdateCvssVectorErrorComponent
                | ApiV1CvesUpdateDebugModeErrorComponent
                | ApiV1CvesUpdateDescriptionErrorComponent
                | ApiV1CvesUpdateDiscoveryEnabledErrorComponent
                | ApiV1CvesUpdateDisplayNameErrorComponent
                | ApiV1CvesUpdateKindErrorComponent
                | ApiV1CvesUpdateLabelsErrorComponent
                | ApiV1CvesUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1CvesUpdateManagedByContentTypeErrorComponent
                | ApiV1CvesUpdateManagedByObjectIdErrorComponent
                | ApiV1CvesUpdateModifiedAtErrorComponent
                | ApiV1CvesUpdateModifiedByUserErrorComponent
                | ApiV1CvesUpdateNameErrorComponent
                | ApiV1CvesUpdateNonFieldErrorsErrorComponent
                | ApiV1CvesUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1CvesUpdatePlatformServiceErrorComponent
                | ApiV1CvesUpdateProviderErrorComponent
                | ApiV1CvesUpdateProviderIdErrorComponent
                | ApiV1CvesUpdateProviderReferenceErrorComponent
                | ApiV1CvesUpdatePublishedAtErrorComponent
                | ApiV1CvesUpdateReconciliationEnabledErrorComponent
                | ApiV1CvesUpdateScopeErrorComponent
                | ApiV1CvesUpdateSeverityErrorComponent
                | ApiV1CvesUpdateSlaAvailabilityErrorComponent
                | ApiV1CvesUpdateSlaTargetErrorComponent
                | ApiV1CvesUpdateSlaWindowDaysErrorComponent
                | ApiV1CvesUpdateSloAvailabilityErrorComponent
                | ApiV1CvesUpdateSloTargetErrorComponent
                | ApiV1CvesUpdateSloWindowDaysErrorComponent
                | ApiV1CvesUpdateStatusErrorComponent
                | ApiV1CvesUpdateTargetAvailabilityErrorComponent
                | ApiV1CvesUpdateTitleErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_0 = (
                        ApiV1CvesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_1 = ApiV1CvesUpdateNameErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_2 = (
                        ApiV1CvesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_3 = ApiV1CvesUpdateLabelsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_4 = (
                        ApiV1CvesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_5 = (
                        ApiV1CvesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_6 = ApiV1CvesUpdateProviderErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_7 = (
                        ApiV1CvesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_8 = (
                        ApiV1CvesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_9 = (
                        ApiV1CvesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_10 = (
                        ApiV1CvesUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_11 = (
                        ApiV1CvesUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_12 = (
                        ApiV1CvesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_13 = ApiV1CvesUpdateScopeErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_14 = ApiV1CvesUpdateKindErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_15 = (
                        ApiV1CvesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_16 = (
                        ApiV1CvesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_17 = (
                        ApiV1CvesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_18 = (
                        ApiV1CvesUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_19 = (
                        ApiV1CvesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_20 = (
                        ApiV1CvesUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_21 = (
                        ApiV1CvesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_22 = (
                        ApiV1CvesUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_23 = (
                        ApiV1CvesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_24 = (
                        ApiV1CvesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_25 = (
                        ApiV1CvesUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_26 = (
                        ApiV1CvesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_27 = (
                        ApiV1CvesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_28 = (
                        ApiV1CvesUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_29 = (
                        ApiV1CvesUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_30 = ApiV1CvesUpdateCveIdErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_31 = ApiV1CvesUpdateTitleErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_32 = (
                        ApiV1CvesUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_33 = (
                        ApiV1CvesUpdatePublishedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_34 = (
                        ApiV1CvesUpdateModifiedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_35 = (
                        ApiV1CvesUpdateCvssScoreErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_36 = (
                        ApiV1CvesUpdateCvssVectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_37 = (
                        ApiV1CvesUpdateSeverityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_38 = ApiV1CvesUpdateStatusErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_39 = (
                        ApiV1CvesUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_40 = (
                        ApiV1CvesUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_update_error_type_41 = (
                        ApiV1CvesUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_cves_update_error_type_42 = (
                    ApiV1CvesUpdateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_cves_update_error_type_42

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_cves_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_cves_update_validation_error.additional_properties = d
        return api_v1_cves_update_validation_error

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
