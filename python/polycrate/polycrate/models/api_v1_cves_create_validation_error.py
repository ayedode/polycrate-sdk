from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_cves_create_actual_availability_error_component import (
        ApiV1CvesCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_create_annotations_error_component import ApiV1CvesCreateAnnotationsErrorComponent
    from ..models.api_v1_cves_create_archived_at_error_component import ApiV1CvesCreateArchivedAtErrorComponent
    from ..models.api_v1_cves_create_archived_by_error_component import ApiV1CvesCreateArchivedByErrorComponent
    from ..models.api_v1_cves_create_archived_error_component import ApiV1CvesCreateArchivedErrorComponent
    from ..models.api_v1_cves_create_archived_reason_error_component import ApiV1CvesCreateArchivedReasonErrorComponent
    from ..models.api_v1_cves_create_created_by_component_error_component import (
        ApiV1CvesCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_cves_create_created_by_user_error_component import ApiV1CvesCreateCreatedByUserErrorComponent
    from ..models.api_v1_cves_create_criticality_error_component import ApiV1CvesCreateCriticalityErrorComponent
    from ..models.api_v1_cves_create_cve_id_error_component import ApiV1CvesCreateCveIdErrorComponent
    from ..models.api_v1_cves_create_cvss_score_error_component import ApiV1CvesCreateCvssScoreErrorComponent
    from ..models.api_v1_cves_create_cvss_vector_error_component import ApiV1CvesCreateCvssVectorErrorComponent
    from ..models.api_v1_cves_create_debug_mode_error_component import ApiV1CvesCreateDebugModeErrorComponent
    from ..models.api_v1_cves_create_description_error_component import ApiV1CvesCreateDescriptionErrorComponent
    from ..models.api_v1_cves_create_discovery_enabled_error_component import (
        ApiV1CvesCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_cves_create_display_name_error_component import ApiV1CvesCreateDisplayNameErrorComponent
    from ..models.api_v1_cves_create_kind_error_component import ApiV1CvesCreateKindErrorComponent
    from ..models.api_v1_cves_create_labels_error_component import ApiV1CvesCreateLabelsErrorComponent
    from ..models.api_v1_cves_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1CvesCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_cves_create_managed_by_content_type_error_component import (
        ApiV1CvesCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_cves_create_managed_by_object_id_error_component import (
        ApiV1CvesCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_cves_create_modified_at_error_component import ApiV1CvesCreateModifiedAtErrorComponent
    from ..models.api_v1_cves_create_modified_by_user_error_component import ApiV1CvesCreateModifiedByUserErrorComponent
    from ..models.api_v1_cves_create_name_error_component import ApiV1CvesCreateNameErrorComponent
    from ..models.api_v1_cves_create_non_field_errors_error_component import ApiV1CvesCreateNonFieldErrorsErrorComponent
    from ..models.api_v1_cves_create_platform_dns_record_created_error_component import (
        ApiV1CvesCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_cves_create_platform_service_error_component import (
        ApiV1CvesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_cves_create_provider_error_component import ApiV1CvesCreateProviderErrorComponent
    from ..models.api_v1_cves_create_provider_id_error_component import ApiV1CvesCreateProviderIdErrorComponent
    from ..models.api_v1_cves_create_provider_reference_error_component import (
        ApiV1CvesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_cves_create_published_at_error_component import ApiV1CvesCreatePublishedAtErrorComponent
    from ..models.api_v1_cves_create_reconciliation_enabled_error_component import (
        ApiV1CvesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_cves_create_scope_error_component import ApiV1CvesCreateScopeErrorComponent
    from ..models.api_v1_cves_create_severity_error_component import ApiV1CvesCreateSeverityErrorComponent
    from ..models.api_v1_cves_create_sla_availability_error_component import (
        ApiV1CvesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_create_sla_target_error_component import ApiV1CvesCreateSlaTargetErrorComponent
    from ..models.api_v1_cves_create_sla_window_days_error_component import ApiV1CvesCreateSlaWindowDaysErrorComponent
    from ..models.api_v1_cves_create_slo_availability_error_component import (
        ApiV1CvesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_create_slo_target_error_component import ApiV1CvesCreateSloTargetErrorComponent
    from ..models.api_v1_cves_create_slo_window_days_error_component import ApiV1CvesCreateSloWindowDaysErrorComponent
    from ..models.api_v1_cves_create_status_error_component import ApiV1CvesCreateStatusErrorComponent
    from ..models.api_v1_cves_create_target_availability_error_component import (
        ApiV1CvesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_create_title_error_component import ApiV1CvesCreateTitleErrorComponent


T = TypeVar("T", bound="ApiV1CvesCreateValidationError")


@_attrs_define
class ApiV1CvesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CvesCreateActualAvailabilityErrorComponent | ApiV1CvesCreateAnnotationsErrorComponent |
            ApiV1CvesCreateArchivedAtErrorComponent | ApiV1CvesCreateArchivedByErrorComponent |
            ApiV1CvesCreateArchivedErrorComponent | ApiV1CvesCreateArchivedReasonErrorComponent |
            ApiV1CvesCreateCreatedByComponentErrorComponent | ApiV1CvesCreateCreatedByUserErrorComponent |
            ApiV1CvesCreateCriticalityErrorComponent | ApiV1CvesCreateCveIdErrorComponent |
            ApiV1CvesCreateCvssScoreErrorComponent | ApiV1CvesCreateCvssVectorErrorComponent |
            ApiV1CvesCreateDebugModeErrorComponent | ApiV1CvesCreateDescriptionErrorComponent |
            ApiV1CvesCreateDiscoveryEnabledErrorComponent | ApiV1CvesCreateDisplayNameErrorComponent |
            ApiV1CvesCreateKindErrorComponent | ApiV1CvesCreateLabelsErrorComponent |
            ApiV1CvesCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1CvesCreateManagedByContentTypeErrorComponent | ApiV1CvesCreateManagedByObjectIdErrorComponent |
            ApiV1CvesCreateModifiedAtErrorComponent | ApiV1CvesCreateModifiedByUserErrorComponent |
            ApiV1CvesCreateNameErrorComponent | ApiV1CvesCreateNonFieldErrorsErrorComponent |
            ApiV1CvesCreatePlatformDnsRecordCreatedErrorComponent | ApiV1CvesCreatePlatformServiceErrorComponent |
            ApiV1CvesCreateProviderErrorComponent | ApiV1CvesCreateProviderIdErrorComponent |
            ApiV1CvesCreateProviderReferenceErrorComponent | ApiV1CvesCreatePublishedAtErrorComponent |
            ApiV1CvesCreateReconciliationEnabledErrorComponent | ApiV1CvesCreateScopeErrorComponent |
            ApiV1CvesCreateSeverityErrorComponent | ApiV1CvesCreateSlaAvailabilityErrorComponent |
            ApiV1CvesCreateSlaTargetErrorComponent | ApiV1CvesCreateSlaWindowDaysErrorComponent |
            ApiV1CvesCreateSloAvailabilityErrorComponent | ApiV1CvesCreateSloTargetErrorComponent |
            ApiV1CvesCreateSloWindowDaysErrorComponent | ApiV1CvesCreateStatusErrorComponent |
            ApiV1CvesCreateTargetAvailabilityErrorComponent | ApiV1CvesCreateTitleErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CvesCreateActualAvailabilityErrorComponent
        | ApiV1CvesCreateAnnotationsErrorComponent
        | ApiV1CvesCreateArchivedAtErrorComponent
        | ApiV1CvesCreateArchivedByErrorComponent
        | ApiV1CvesCreateArchivedErrorComponent
        | ApiV1CvesCreateArchivedReasonErrorComponent
        | ApiV1CvesCreateCreatedByComponentErrorComponent
        | ApiV1CvesCreateCreatedByUserErrorComponent
        | ApiV1CvesCreateCriticalityErrorComponent
        | ApiV1CvesCreateCveIdErrorComponent
        | ApiV1CvesCreateCvssScoreErrorComponent
        | ApiV1CvesCreateCvssVectorErrorComponent
        | ApiV1CvesCreateDebugModeErrorComponent
        | ApiV1CvesCreateDescriptionErrorComponent
        | ApiV1CvesCreateDiscoveryEnabledErrorComponent
        | ApiV1CvesCreateDisplayNameErrorComponent
        | ApiV1CvesCreateKindErrorComponent
        | ApiV1CvesCreateLabelsErrorComponent
        | ApiV1CvesCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1CvesCreateManagedByContentTypeErrorComponent
        | ApiV1CvesCreateManagedByObjectIdErrorComponent
        | ApiV1CvesCreateModifiedAtErrorComponent
        | ApiV1CvesCreateModifiedByUserErrorComponent
        | ApiV1CvesCreateNameErrorComponent
        | ApiV1CvesCreateNonFieldErrorsErrorComponent
        | ApiV1CvesCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1CvesCreatePlatformServiceErrorComponent
        | ApiV1CvesCreateProviderErrorComponent
        | ApiV1CvesCreateProviderIdErrorComponent
        | ApiV1CvesCreateProviderReferenceErrorComponent
        | ApiV1CvesCreatePublishedAtErrorComponent
        | ApiV1CvesCreateReconciliationEnabledErrorComponent
        | ApiV1CvesCreateScopeErrorComponent
        | ApiV1CvesCreateSeverityErrorComponent
        | ApiV1CvesCreateSlaAvailabilityErrorComponent
        | ApiV1CvesCreateSlaTargetErrorComponent
        | ApiV1CvesCreateSlaWindowDaysErrorComponent
        | ApiV1CvesCreateSloAvailabilityErrorComponent
        | ApiV1CvesCreateSloTargetErrorComponent
        | ApiV1CvesCreateSloWindowDaysErrorComponent
        | ApiV1CvesCreateStatusErrorComponent
        | ApiV1CvesCreateTargetAvailabilityErrorComponent
        | ApiV1CvesCreateTitleErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_cves_create_actual_availability_error_component import (
            ApiV1CvesCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_annotations_error_component import (
            ApiV1CvesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_archived_at_error_component import (
            ApiV1CvesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_archived_by_error_component import (
            ApiV1CvesCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_archived_error_component import (
            ApiV1CvesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_archived_reason_error_component import (
            ApiV1CvesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_created_by_component_error_component import (
            ApiV1CvesCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_criticality_error_component import (
            ApiV1CvesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_cve_id_error_component import (
            ApiV1CvesCreateCveIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_cvss_score_error_component import (
            ApiV1CvesCreateCvssScoreErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_cvss_vector_error_component import (
            ApiV1CvesCreateCvssVectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_debug_mode_error_component import (
            ApiV1CvesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_description_error_component import (
            ApiV1CvesCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_discovery_enabled_error_component import (
            ApiV1CvesCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_display_name_error_component import (
            ApiV1CvesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_kind_error_component import ApiV1CvesCreateKindErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_create_labels_error_component import (
            ApiV1CvesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1CvesCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_managed_by_content_type_error_component import (
            ApiV1CvesCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_managed_by_object_id_error_component import (
            ApiV1CvesCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_modified_at_error_component import (
            ApiV1CvesCreateModifiedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_modified_by_user_error_component import (
            ApiV1CvesCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_name_error_component import ApiV1CvesCreateNameErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_create_non_field_errors_error_component import (
            ApiV1CvesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_platform_dns_record_created_error_component import (
            ApiV1CvesCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_platform_service_error_component import (
            ApiV1CvesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_provider_error_component import (
            ApiV1CvesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_provider_id_error_component import (
            ApiV1CvesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_provider_reference_error_component import (
            ApiV1CvesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_published_at_error_component import (
            ApiV1CvesCreatePublishedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_reconciliation_enabled_error_component import (
            ApiV1CvesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_scope_error_component import (
            ApiV1CvesCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_severity_error_component import (
            ApiV1CvesCreateSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_sla_availability_error_component import (
            ApiV1CvesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_sla_target_error_component import (
            ApiV1CvesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_sla_window_days_error_component import (
            ApiV1CvesCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_slo_availability_error_component import (
            ApiV1CvesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_slo_target_error_component import (
            ApiV1CvesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_slo_window_days_error_component import (
            ApiV1CvesCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_status_error_component import (
            ApiV1CvesCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_target_availability_error_component import (
            ApiV1CvesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_title_error_component import (
            ApiV1CvesCreateTitleErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CvesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateCveIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateTitleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreatePublishedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateModifiedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateCvssScoreErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateCvssVectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateSeverityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesCreateModifiedByUserErrorComponent):
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
        from ..models.api_v1_cves_create_actual_availability_error_component import (
            ApiV1CvesCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_annotations_error_component import (
            ApiV1CvesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_archived_at_error_component import (
            ApiV1CvesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_archived_by_error_component import (
            ApiV1CvesCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_archived_error_component import (
            ApiV1CvesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_archived_reason_error_component import (
            ApiV1CvesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_created_by_component_error_component import (
            ApiV1CvesCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_created_by_user_error_component import (
            ApiV1CvesCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_criticality_error_component import (
            ApiV1CvesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_cve_id_error_component import (
            ApiV1CvesCreateCveIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_cvss_score_error_component import (
            ApiV1CvesCreateCvssScoreErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_cvss_vector_error_component import (
            ApiV1CvesCreateCvssVectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_debug_mode_error_component import (
            ApiV1CvesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_description_error_component import (
            ApiV1CvesCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_discovery_enabled_error_component import (
            ApiV1CvesCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_display_name_error_component import (
            ApiV1CvesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_kind_error_component import ApiV1CvesCreateKindErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_create_labels_error_component import (
            ApiV1CvesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1CvesCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_managed_by_content_type_error_component import (
            ApiV1CvesCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_managed_by_object_id_error_component import (
            ApiV1CvesCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_modified_at_error_component import (
            ApiV1CvesCreateModifiedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_modified_by_user_error_component import (
            ApiV1CvesCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_name_error_component import ApiV1CvesCreateNameErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_create_non_field_errors_error_component import (
            ApiV1CvesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_platform_dns_record_created_error_component import (
            ApiV1CvesCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_platform_service_error_component import (
            ApiV1CvesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_provider_error_component import (
            ApiV1CvesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_provider_id_error_component import (
            ApiV1CvesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_provider_reference_error_component import (
            ApiV1CvesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_published_at_error_component import (
            ApiV1CvesCreatePublishedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_reconciliation_enabled_error_component import (
            ApiV1CvesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_scope_error_component import (
            ApiV1CvesCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_severity_error_component import (
            ApiV1CvesCreateSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_sla_availability_error_component import (
            ApiV1CvesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_sla_target_error_component import (
            ApiV1CvesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_sla_window_days_error_component import (
            ApiV1CvesCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_slo_availability_error_component import (
            ApiV1CvesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_slo_target_error_component import (
            ApiV1CvesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_slo_window_days_error_component import (
            ApiV1CvesCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_status_error_component import (
            ApiV1CvesCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_target_availability_error_component import (
            ApiV1CvesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_create_title_error_component import (
            ApiV1CvesCreateTitleErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CvesCreateActualAvailabilityErrorComponent
                | ApiV1CvesCreateAnnotationsErrorComponent
                | ApiV1CvesCreateArchivedAtErrorComponent
                | ApiV1CvesCreateArchivedByErrorComponent
                | ApiV1CvesCreateArchivedErrorComponent
                | ApiV1CvesCreateArchivedReasonErrorComponent
                | ApiV1CvesCreateCreatedByComponentErrorComponent
                | ApiV1CvesCreateCreatedByUserErrorComponent
                | ApiV1CvesCreateCriticalityErrorComponent
                | ApiV1CvesCreateCveIdErrorComponent
                | ApiV1CvesCreateCvssScoreErrorComponent
                | ApiV1CvesCreateCvssVectorErrorComponent
                | ApiV1CvesCreateDebugModeErrorComponent
                | ApiV1CvesCreateDescriptionErrorComponent
                | ApiV1CvesCreateDiscoveryEnabledErrorComponent
                | ApiV1CvesCreateDisplayNameErrorComponent
                | ApiV1CvesCreateKindErrorComponent
                | ApiV1CvesCreateLabelsErrorComponent
                | ApiV1CvesCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1CvesCreateManagedByContentTypeErrorComponent
                | ApiV1CvesCreateManagedByObjectIdErrorComponent
                | ApiV1CvesCreateModifiedAtErrorComponent
                | ApiV1CvesCreateModifiedByUserErrorComponent
                | ApiV1CvesCreateNameErrorComponent
                | ApiV1CvesCreateNonFieldErrorsErrorComponent
                | ApiV1CvesCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1CvesCreatePlatformServiceErrorComponent
                | ApiV1CvesCreateProviderErrorComponent
                | ApiV1CvesCreateProviderIdErrorComponent
                | ApiV1CvesCreateProviderReferenceErrorComponent
                | ApiV1CvesCreatePublishedAtErrorComponent
                | ApiV1CvesCreateReconciliationEnabledErrorComponent
                | ApiV1CvesCreateScopeErrorComponent
                | ApiV1CvesCreateSeverityErrorComponent
                | ApiV1CvesCreateSlaAvailabilityErrorComponent
                | ApiV1CvesCreateSlaTargetErrorComponent
                | ApiV1CvesCreateSlaWindowDaysErrorComponent
                | ApiV1CvesCreateSloAvailabilityErrorComponent
                | ApiV1CvesCreateSloTargetErrorComponent
                | ApiV1CvesCreateSloWindowDaysErrorComponent
                | ApiV1CvesCreateStatusErrorComponent
                | ApiV1CvesCreateTargetAvailabilityErrorComponent
                | ApiV1CvesCreateTitleErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_0 = (
                        ApiV1CvesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_1 = ApiV1CvesCreateNameErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_2 = (
                        ApiV1CvesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_3 = ApiV1CvesCreateLabelsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_4 = (
                        ApiV1CvesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_5 = (
                        ApiV1CvesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_6 = ApiV1CvesCreateProviderErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_7 = (
                        ApiV1CvesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_8 = (
                        ApiV1CvesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_9 = (
                        ApiV1CvesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_10 = (
                        ApiV1CvesCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_11 = (
                        ApiV1CvesCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_12 = (
                        ApiV1CvesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_13 = ApiV1CvesCreateScopeErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_14 = ApiV1CvesCreateKindErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_15 = (
                        ApiV1CvesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_16 = (
                        ApiV1CvesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_17 = (
                        ApiV1CvesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_18 = (
                        ApiV1CvesCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_19 = (
                        ApiV1CvesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_20 = (
                        ApiV1CvesCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_21 = (
                        ApiV1CvesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_22 = (
                        ApiV1CvesCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_23 = (
                        ApiV1CvesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_24 = (
                        ApiV1CvesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_25 = (
                        ApiV1CvesCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_26 = (
                        ApiV1CvesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_27 = (
                        ApiV1CvesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_28 = (
                        ApiV1CvesCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_29 = (
                        ApiV1CvesCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_30 = ApiV1CvesCreateCveIdErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_31 = ApiV1CvesCreateTitleErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_32 = (
                        ApiV1CvesCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_33 = (
                        ApiV1CvesCreatePublishedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_34 = (
                        ApiV1CvesCreateModifiedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_35 = (
                        ApiV1CvesCreateCvssScoreErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_36 = (
                        ApiV1CvesCreateCvssVectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_37 = (
                        ApiV1CvesCreateSeverityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_38 = ApiV1CvesCreateStatusErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_39 = (
                        ApiV1CvesCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_40 = (
                        ApiV1CvesCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_create_error_type_41 = (
                        ApiV1CvesCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_cves_create_error_type_42 = (
                    ApiV1CvesCreateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_cves_create_error_type_42

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_cves_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_cves_create_validation_error.additional_properties = d
        return api_v1_cves_create_validation_error

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
