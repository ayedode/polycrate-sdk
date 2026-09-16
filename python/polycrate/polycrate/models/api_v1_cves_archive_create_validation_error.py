from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_cves_archive_create_actual_availability_error_component import (
        ApiV1CvesArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_annotations_error_component import (
        ApiV1CvesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_archived_at_error_component import (
        ApiV1CvesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_archived_by_error_component import (
        ApiV1CvesArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_archived_error_component import (
        ApiV1CvesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_archived_reason_error_component import (
        ApiV1CvesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_created_by_component_error_component import (
        ApiV1CvesArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_created_by_user_error_component import (
        ApiV1CvesArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_criticality_error_component import (
        ApiV1CvesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_cve_id_error_component import ApiV1CvesArchiveCreateCveIdErrorComponent
    from ..models.api_v1_cves_archive_create_cvss_score_error_component import (
        ApiV1CvesArchiveCreateCvssScoreErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_cvss_vector_error_component import (
        ApiV1CvesArchiveCreateCvssVectorErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_debug_mode_error_component import (
        ApiV1CvesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_description_error_component import (
        ApiV1CvesArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_discovery_enabled_error_component import (
        ApiV1CvesArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_display_name_error_component import (
        ApiV1CvesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_kind_error_component import ApiV1CvesArchiveCreateKindErrorComponent
    from ..models.api_v1_cves_archive_create_labels_error_component import ApiV1CvesArchiveCreateLabelsErrorComponent
    from ..models.api_v1_cves_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1CvesArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_managed_by_content_type_error_component import (
        ApiV1CvesArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_managed_by_object_id_error_component import (
        ApiV1CvesArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_modified_at_error_component import (
        ApiV1CvesArchiveCreateModifiedAtErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_modified_by_user_error_component import (
        ApiV1CvesArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_name_error_component import ApiV1CvesArchiveCreateNameErrorComponent
    from ..models.api_v1_cves_archive_create_non_field_errors_error_component import (
        ApiV1CvesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_platform_dns_record_created_error_component import (
        ApiV1CvesArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_platform_service_error_component import (
        ApiV1CvesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_provider_error_component import (
        ApiV1CvesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_provider_id_error_component import (
        ApiV1CvesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_provider_reference_error_component import (
        ApiV1CvesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_published_at_error_component import (
        ApiV1CvesArchiveCreatePublishedAtErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_reconciliation_enabled_error_component import (
        ApiV1CvesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_scope_error_component import ApiV1CvesArchiveCreateScopeErrorComponent
    from ..models.api_v1_cves_archive_create_severity_error_component import (
        ApiV1CvesArchiveCreateSeverityErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_sla_availability_error_component import (
        ApiV1CvesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_sla_target_error_component import (
        ApiV1CvesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_sla_window_days_error_component import (
        ApiV1CvesArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_slo_availability_error_component import (
        ApiV1CvesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_slo_target_error_component import (
        ApiV1CvesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_slo_window_days_error_component import (
        ApiV1CvesArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_status_error_component import ApiV1CvesArchiveCreateStatusErrorComponent
    from ..models.api_v1_cves_archive_create_target_availability_error_component import (
        ApiV1CvesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_cves_archive_create_title_error_component import ApiV1CvesArchiveCreateTitleErrorComponent


T = TypeVar("T", bound="ApiV1CvesArchiveCreateValidationError")


@_attrs_define
class ApiV1CvesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CvesArchiveCreateActualAvailabilityErrorComponent |
            ApiV1CvesArchiveCreateAnnotationsErrorComponent | ApiV1CvesArchiveCreateArchivedAtErrorComponent |
            ApiV1CvesArchiveCreateArchivedByErrorComponent | ApiV1CvesArchiveCreateArchivedErrorComponent |
            ApiV1CvesArchiveCreateArchivedReasonErrorComponent | ApiV1CvesArchiveCreateCreatedByComponentErrorComponent |
            ApiV1CvesArchiveCreateCreatedByUserErrorComponent | ApiV1CvesArchiveCreateCriticalityErrorComponent |
            ApiV1CvesArchiveCreateCveIdErrorComponent | ApiV1CvesArchiveCreateCvssScoreErrorComponent |
            ApiV1CvesArchiveCreateCvssVectorErrorComponent | ApiV1CvesArchiveCreateDebugModeErrorComponent |
            ApiV1CvesArchiveCreateDescriptionErrorComponent | ApiV1CvesArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1CvesArchiveCreateDisplayNameErrorComponent | ApiV1CvesArchiveCreateKindErrorComponent |
            ApiV1CvesArchiveCreateLabelsErrorComponent |
            ApiV1CvesArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1CvesArchiveCreateManagedByContentTypeErrorComponent | ApiV1CvesArchiveCreateManagedByObjectIdErrorComponent
            | ApiV1CvesArchiveCreateModifiedAtErrorComponent | ApiV1CvesArchiveCreateModifiedByUserErrorComponent |
            ApiV1CvesArchiveCreateNameErrorComponent | ApiV1CvesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1CvesArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1CvesArchiveCreatePlatformServiceErrorComponent | ApiV1CvesArchiveCreateProviderErrorComponent |
            ApiV1CvesArchiveCreateProviderIdErrorComponent | ApiV1CvesArchiveCreateProviderReferenceErrorComponent |
            ApiV1CvesArchiveCreatePublishedAtErrorComponent | ApiV1CvesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1CvesArchiveCreateScopeErrorComponent | ApiV1CvesArchiveCreateSeverityErrorComponent |
            ApiV1CvesArchiveCreateSlaAvailabilityErrorComponent | ApiV1CvesArchiveCreateSlaTargetErrorComponent |
            ApiV1CvesArchiveCreateSlaWindowDaysErrorComponent | ApiV1CvesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1CvesArchiveCreateSloTargetErrorComponent | ApiV1CvesArchiveCreateSloWindowDaysErrorComponent |
            ApiV1CvesArchiveCreateStatusErrorComponent | ApiV1CvesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1CvesArchiveCreateTitleErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CvesArchiveCreateActualAvailabilityErrorComponent
        | ApiV1CvesArchiveCreateAnnotationsErrorComponent
        | ApiV1CvesArchiveCreateArchivedAtErrorComponent
        | ApiV1CvesArchiveCreateArchivedByErrorComponent
        | ApiV1CvesArchiveCreateArchivedErrorComponent
        | ApiV1CvesArchiveCreateArchivedReasonErrorComponent
        | ApiV1CvesArchiveCreateCreatedByComponentErrorComponent
        | ApiV1CvesArchiveCreateCreatedByUserErrorComponent
        | ApiV1CvesArchiveCreateCriticalityErrorComponent
        | ApiV1CvesArchiveCreateCveIdErrorComponent
        | ApiV1CvesArchiveCreateCvssScoreErrorComponent
        | ApiV1CvesArchiveCreateCvssVectorErrorComponent
        | ApiV1CvesArchiveCreateDebugModeErrorComponent
        | ApiV1CvesArchiveCreateDescriptionErrorComponent
        | ApiV1CvesArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1CvesArchiveCreateDisplayNameErrorComponent
        | ApiV1CvesArchiveCreateKindErrorComponent
        | ApiV1CvesArchiveCreateLabelsErrorComponent
        | ApiV1CvesArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1CvesArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1CvesArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1CvesArchiveCreateModifiedAtErrorComponent
        | ApiV1CvesArchiveCreateModifiedByUserErrorComponent
        | ApiV1CvesArchiveCreateNameErrorComponent
        | ApiV1CvesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1CvesArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1CvesArchiveCreatePlatformServiceErrorComponent
        | ApiV1CvesArchiveCreateProviderErrorComponent
        | ApiV1CvesArchiveCreateProviderIdErrorComponent
        | ApiV1CvesArchiveCreateProviderReferenceErrorComponent
        | ApiV1CvesArchiveCreatePublishedAtErrorComponent
        | ApiV1CvesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1CvesArchiveCreateScopeErrorComponent
        | ApiV1CvesArchiveCreateSeverityErrorComponent
        | ApiV1CvesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1CvesArchiveCreateSlaTargetErrorComponent
        | ApiV1CvesArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1CvesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1CvesArchiveCreateSloTargetErrorComponent
        | ApiV1CvesArchiveCreateSloWindowDaysErrorComponent
        | ApiV1CvesArchiveCreateStatusErrorComponent
        | ApiV1CvesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1CvesArchiveCreateTitleErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_cves_archive_create_actual_availability_error_component import (
            ApiV1CvesArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_annotations_error_component import (
            ApiV1CvesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_archived_at_error_component import (
            ApiV1CvesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_archived_by_error_component import (
            ApiV1CvesArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_archived_error_component import (
            ApiV1CvesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_archived_reason_error_component import (
            ApiV1CvesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_created_by_component_error_component import (
            ApiV1CvesArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_criticality_error_component import (
            ApiV1CvesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_cve_id_error_component import (
            ApiV1CvesArchiveCreateCveIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_cvss_score_error_component import (
            ApiV1CvesArchiveCreateCvssScoreErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_cvss_vector_error_component import (
            ApiV1CvesArchiveCreateCvssVectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_debug_mode_error_component import (
            ApiV1CvesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_description_error_component import (
            ApiV1CvesArchiveCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_discovery_enabled_error_component import (
            ApiV1CvesArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_display_name_error_component import (
            ApiV1CvesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_kind_error_component import (
            ApiV1CvesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_labels_error_component import (
            ApiV1CvesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1CvesArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_managed_by_content_type_error_component import (
            ApiV1CvesArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_managed_by_object_id_error_component import (
            ApiV1CvesArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_modified_at_error_component import (
            ApiV1CvesArchiveCreateModifiedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_modified_by_user_error_component import (
            ApiV1CvesArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_name_error_component import (
            ApiV1CvesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_non_field_errors_error_component import (
            ApiV1CvesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_platform_dns_record_created_error_component import (
            ApiV1CvesArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_platform_service_error_component import (
            ApiV1CvesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_provider_error_component import (
            ApiV1CvesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_provider_id_error_component import (
            ApiV1CvesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_provider_reference_error_component import (
            ApiV1CvesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_published_at_error_component import (
            ApiV1CvesArchiveCreatePublishedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_reconciliation_enabled_error_component import (
            ApiV1CvesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_scope_error_component import (
            ApiV1CvesArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_severity_error_component import (
            ApiV1CvesArchiveCreateSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_sla_availability_error_component import (
            ApiV1CvesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_sla_target_error_component import (
            ApiV1CvesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_sla_window_days_error_component import (
            ApiV1CvesArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_slo_availability_error_component import (
            ApiV1CvesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_slo_target_error_component import (
            ApiV1CvesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_slo_window_days_error_component import (
            ApiV1CvesArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_status_error_component import (
            ApiV1CvesArchiveCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_target_availability_error_component import (
            ApiV1CvesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_title_error_component import (
            ApiV1CvesArchiveCreateTitleErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CvesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateCveIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateTitleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreatePublishedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateModifiedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateCvssScoreErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateCvssVectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateSeverityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesArchiveCreateModifiedByUserErrorComponent):
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
        from ..models.api_v1_cves_archive_create_actual_availability_error_component import (
            ApiV1CvesArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_annotations_error_component import (
            ApiV1CvesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_archived_at_error_component import (
            ApiV1CvesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_archived_by_error_component import (
            ApiV1CvesArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_archived_error_component import (
            ApiV1CvesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_archived_reason_error_component import (
            ApiV1CvesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_created_by_component_error_component import (
            ApiV1CvesArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_created_by_user_error_component import (
            ApiV1CvesArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_criticality_error_component import (
            ApiV1CvesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_cve_id_error_component import (
            ApiV1CvesArchiveCreateCveIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_cvss_score_error_component import (
            ApiV1CvesArchiveCreateCvssScoreErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_cvss_vector_error_component import (
            ApiV1CvesArchiveCreateCvssVectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_debug_mode_error_component import (
            ApiV1CvesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_description_error_component import (
            ApiV1CvesArchiveCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_discovery_enabled_error_component import (
            ApiV1CvesArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_display_name_error_component import (
            ApiV1CvesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_kind_error_component import (
            ApiV1CvesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_labels_error_component import (
            ApiV1CvesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1CvesArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_managed_by_content_type_error_component import (
            ApiV1CvesArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_managed_by_object_id_error_component import (
            ApiV1CvesArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_modified_at_error_component import (
            ApiV1CvesArchiveCreateModifiedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_modified_by_user_error_component import (
            ApiV1CvesArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_name_error_component import (
            ApiV1CvesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_non_field_errors_error_component import (
            ApiV1CvesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_platform_dns_record_created_error_component import (
            ApiV1CvesArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_platform_service_error_component import (
            ApiV1CvesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_provider_error_component import (
            ApiV1CvesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_provider_id_error_component import (
            ApiV1CvesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_provider_reference_error_component import (
            ApiV1CvesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_published_at_error_component import (
            ApiV1CvesArchiveCreatePublishedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_reconciliation_enabled_error_component import (
            ApiV1CvesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_scope_error_component import (
            ApiV1CvesArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_severity_error_component import (
            ApiV1CvesArchiveCreateSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_sla_availability_error_component import (
            ApiV1CvesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_sla_target_error_component import (
            ApiV1CvesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_sla_window_days_error_component import (
            ApiV1CvesArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_slo_availability_error_component import (
            ApiV1CvesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_slo_target_error_component import (
            ApiV1CvesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_slo_window_days_error_component import (
            ApiV1CvesArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_status_error_component import (
            ApiV1CvesArchiveCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_target_availability_error_component import (
            ApiV1CvesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_archive_create_title_error_component import (
            ApiV1CvesArchiveCreateTitleErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CvesArchiveCreateActualAvailabilityErrorComponent
                | ApiV1CvesArchiveCreateAnnotationsErrorComponent
                | ApiV1CvesArchiveCreateArchivedAtErrorComponent
                | ApiV1CvesArchiveCreateArchivedByErrorComponent
                | ApiV1CvesArchiveCreateArchivedErrorComponent
                | ApiV1CvesArchiveCreateArchivedReasonErrorComponent
                | ApiV1CvesArchiveCreateCreatedByComponentErrorComponent
                | ApiV1CvesArchiveCreateCreatedByUserErrorComponent
                | ApiV1CvesArchiveCreateCriticalityErrorComponent
                | ApiV1CvesArchiveCreateCveIdErrorComponent
                | ApiV1CvesArchiveCreateCvssScoreErrorComponent
                | ApiV1CvesArchiveCreateCvssVectorErrorComponent
                | ApiV1CvesArchiveCreateDebugModeErrorComponent
                | ApiV1CvesArchiveCreateDescriptionErrorComponent
                | ApiV1CvesArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1CvesArchiveCreateDisplayNameErrorComponent
                | ApiV1CvesArchiveCreateKindErrorComponent
                | ApiV1CvesArchiveCreateLabelsErrorComponent
                | ApiV1CvesArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1CvesArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1CvesArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1CvesArchiveCreateModifiedAtErrorComponent
                | ApiV1CvesArchiveCreateModifiedByUserErrorComponent
                | ApiV1CvesArchiveCreateNameErrorComponent
                | ApiV1CvesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1CvesArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1CvesArchiveCreatePlatformServiceErrorComponent
                | ApiV1CvesArchiveCreateProviderErrorComponent
                | ApiV1CvesArchiveCreateProviderIdErrorComponent
                | ApiV1CvesArchiveCreateProviderReferenceErrorComponent
                | ApiV1CvesArchiveCreatePublishedAtErrorComponent
                | ApiV1CvesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1CvesArchiveCreateScopeErrorComponent
                | ApiV1CvesArchiveCreateSeverityErrorComponent
                | ApiV1CvesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1CvesArchiveCreateSlaTargetErrorComponent
                | ApiV1CvesArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1CvesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1CvesArchiveCreateSloTargetErrorComponent
                | ApiV1CvesArchiveCreateSloWindowDaysErrorComponent
                | ApiV1CvesArchiveCreateStatusErrorComponent
                | ApiV1CvesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1CvesArchiveCreateTitleErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_0 = (
                        ApiV1CvesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_1 = (
                        ApiV1CvesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_2 = (
                        ApiV1CvesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_3 = (
                        ApiV1CvesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_4 = (
                        ApiV1CvesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_5 = (
                        ApiV1CvesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_6 = (
                        ApiV1CvesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_7 = (
                        ApiV1CvesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_8 = (
                        ApiV1CvesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_9 = (
                        ApiV1CvesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_10 = (
                        ApiV1CvesArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_11 = (
                        ApiV1CvesArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_12 = (
                        ApiV1CvesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_13 = (
                        ApiV1CvesArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_14 = (
                        ApiV1CvesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_15 = (
                        ApiV1CvesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_16 = (
                        ApiV1CvesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_17 = (
                        ApiV1CvesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_18 = (
                        ApiV1CvesArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_19 = (
                        ApiV1CvesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_20 = (
                        ApiV1CvesArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_21 = (
                        ApiV1CvesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_22 = (
                        ApiV1CvesArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_23 = (
                        ApiV1CvesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_24 = (
                        ApiV1CvesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_25 = (
                        ApiV1CvesArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_26 = (
                        ApiV1CvesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_27 = (
                        ApiV1CvesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_28 = (
                        ApiV1CvesArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_29 = (
                        ApiV1CvesArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_30 = (
                        ApiV1CvesArchiveCreateCveIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_31 = (
                        ApiV1CvesArchiveCreateTitleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_32 = (
                        ApiV1CvesArchiveCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_33 = (
                        ApiV1CvesArchiveCreatePublishedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_34 = (
                        ApiV1CvesArchiveCreateModifiedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_35 = (
                        ApiV1CvesArchiveCreateCvssScoreErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_36 = (
                        ApiV1CvesArchiveCreateCvssVectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_37 = (
                        ApiV1CvesArchiveCreateSeverityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_38 = (
                        ApiV1CvesArchiveCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_39 = (
                        ApiV1CvesArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_40 = (
                        ApiV1CvesArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_archive_create_error_type_41 = (
                        ApiV1CvesArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_cves_archive_create_error_type_42 = (
                    ApiV1CvesArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_cves_archive_create_error_type_42

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_cves_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_cves_archive_create_validation_error.additional_properties = d
        return api_v1_cves_archive_create_validation_error

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
